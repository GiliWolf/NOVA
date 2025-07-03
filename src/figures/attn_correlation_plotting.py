import os
import sys

sys.path.insert(1, os.getenv("NOVA_HOME"))
print(f"NOVA_HOME: {os.getenv('NOVA_HOME')}")
import logging
import numpy as np
import matplotlib.pyplot as plt
import os
from typing import List, Tuple, Iterable, Dict
import torch
from src.datasets.dataset_config import DatasetConfig
from src.figures.plot_correlation_config import PlotCorrConfig
from src.datasets.label_utils import get_unique_parts_from_labels, get_markers_from_labels, get_batches_from_labels

def plot_correlation(corr_data, corr_method, config_plot, channel_names=None,
                     sup_title="Correlation", output_folder_path=None, per_layer=False):

    # Step 1: Normalize shape to (N, C, L)
    if corr_data.ndim == 2:
        corr_data = corr_data[:, :, np.newaxis]  # shape (N, C, 1)
        only_one_layer = True
    elif corr_data.ndim == 3:
        only_one_layer = False
    else:
        raise ValueError(f"Unsupported shape for corr_data: {corr_data.shape}")

    num_samples, num_channels, num_layers = corr_data.shape

    # Step 2: Channel names
    if channel_names is None:
        channel_names = [f"Ch{i}" for i in range(num_channels)]
    assert len(channel_names) == num_channels, "Mismatch between channel names and data"

    if per_layer:
        # ─── Line + shaded percentile plot across layers ───
        def get_corr_percentiles(data):
            p25s, medians, p75s = [], [], []
            for ch in range(num_channels):
                p25, med, p75 = get_percentiles(data[:, ch, :], prc_list=[25, 50, 75])
                p25s.append(p25)
                medians.append(med)
                p75s.append(p75)
            return p25s, medians, p75s

        p25s_corr, medians_corr, p75s_corr = get_corr_percentiles(corr_data)
        layers_range = np.arange(num_layers)

        fig, ax = plt.subplots(figsize=(1.5 * num_layers, 6))
        ax.axhline(y=0, color='black', linestyle='--', linewidth=1)

        for ch in range(num_channels):
            ax.plot(layers_range, medians_corr[ch], label=f"{channel_names[ch]} (Median)",
                    marker='o', color=f"C{ch}")
            ax.fill_between(layers_range, p25s_corr[ch], p75s_corr[ch],
                            alpha=0.3, color=f"C{ch}")

        ax.set_xlabel("Layer Number", fontsize=config_plot.PLOT_TITLE_FONTSIZE)
        ax.set_xticks(layers_range)

    else:
        # ─── Boxplot per channel (collapsed over layers) ───
        fig, ax = plt.subplots(figsize=(1.5 * num_channels, 6))
        ax.axhline(y=0, color='black', linestyle='--', linewidth=1)

        for ch in range(num_channels):
            values = corr_data[:, ch, :].flatten()
            ax.boxplot(values,
                       positions=[ch + 1],
                       widths=0.6,
                       patch_artist=True,
                       boxprops=dict(facecolor=f"C{ch}", color='black'),
                       medianprops=dict(color='black'),
                       showfliers=False)

        ax.set_xticks(np.arange(1, num_channels + 1))
        ax.set_xticklabels(channel_names, fontsize=10)

    # ─── Shared formatting ───
    ax.set_ylabel(f"{corr_method} Correlation", fontsize=config_plot.PLOT_TITLE_FONTSIZE)
    ax.set_ylim(-1, 1)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    ax.legend(loc="upper left")
    fig.suptitle(sup_title, fontsize=config_plot.PLOT_SUPTITLE_FONTSIZE)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

    # ─── Save or show ───
    if config_plot.SAVE_PLOT and output_folder_path is not None:
        fig_name = sup_title.split('\n', 1)[0]
        plt.savefig(os.path.join(output_folder_path, f"{fig_name}.png"),
                    dpi=config_plot.PLOT_SAVEFIG_DPI, bbox_inches="tight", facecolor=fig.get_facecolor())
        plt.close()
    else:
        plt.show()




def plot_correlation_by_markers(corr_by_markers, corr_method, config_plot, channel_names=None,
                                sup_title="Correlation_by_Markers", output_folder_path=None,
                                per_layer=False):
    """
    Plots correlation boxplots for each marker group, grouped by marker and channel.

    Parameters:
        corr_by_markers: dict of {marker_name: np.ndarray}, shape (N, C[, L])
        corr_method: string, correlation method name
        config_plot: config object with plotting settings
        channel_names: optional list of names for each correlation channel
        sup_title: title for the plot
        output_folder_path: path to save figure
        per_layer: if True, plots each layer separately instead of collapsing across layers
    """

    marker_names = list(corr_by_markers.keys())
    sample = np.array(next(iter(corr_by_markers.values())))

    # Normalize shape: (N, C) → (N, C, 1)
    if sample.ndim == 2:
        corr_by_markers = {k: v[:, :, np.newaxis] for k, v in corr_by_markers.items()}
        is_rollout = True
    elif sample.ndim == 3:
        is_rollout = False
    else:
        raise ValueError(f"Unsupported shape: {sample.shape}")

    sample = np.array(next(iter(corr_by_markers.values())))
    num_markers = len(marker_names)
    num_channels = sample.shape[1]
    num_layers = sample.shape[2]

    if channel_names is None:
        channel_names = [f"Ch{i}" for i in range(num_channels)]
    assert len(channel_names) == num_channels

    # Plot setup
    if per_layer:
        fig_width = 1.5 * num_markers * num_channels * num_layers
    else:
        fig_width = 1.5 * num_markers * num_channels
    fig, ax = plt.subplots(figsize=(fig_width, 6))

    box_width = 0.6
    intra_gap = 1.0   # spacing between channels
    layer_gap = 0.5   # spacing between layers within a channel
    inter_gap = 2.5   # spacing between markers

    xtick_positions = []
    xtick_labels = []
    current_pos = 1

    for marker in marker_names:
        data = corr_by_markers[marker]  # shape (N, C, L)
        for ch in range(num_channels):
            if per_layer:
                for l in range(num_layers):
                    values = data[:, ch, l]
                    ax.boxplot(values,
                               positions=[current_pos],
                               widths=box_width,
                               patch_artist=True,
                               boxprops=dict(facecolor=f"C{ch}", color='black'),
                               medianprops=dict(color='black'),
                               showfliers=False)
                    xtick_positions.append(current_pos)
                    xtick_labels.append(f"{marker}\n{channel_names[ch]}\nL{l}")
                    current_pos += layer_gap
                current_pos += intra_gap  # extra gap between channels
            else:
                values = data[:, ch, :].flatten()
                ax.boxplot(values,
                           positions=[current_pos],
                           widths=box_width,
                           patch_artist=True,
                           boxprops=dict(facecolor=f"C{ch}", color='black'),
                           medianprops=dict(color='black'),
                           showfliers=False)
                xtick_positions.append(current_pos)
                xtick_labels.append(f"{marker}\n{channel_names[ch]}")
                current_pos += intra_gap
        current_pos += inter_gap  # extra gap between markers

    # Formatting
    ax.axhline(y=0, color='black', linestyle='--', linewidth=1)
    ax.set_xticks(xtick_positions)
    ax.set_xticklabels(xtick_labels, rotation=45, ha='right', fontsize=10)
    ax.set_ylabel(f"{corr_method} Correlation", fontsize=12)
    ax.set_ylim(-1, 1)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    fig.suptitle(sup_title, fontsize=config_plot.PLOT_SUPTITLE_FONTSIZE)

    plt.tight_layout()

    # Save or show
    if config_plot.SAVE_PLOT and output_folder_path is not None:
        fig_name = sup_title.split('\n', 1)[0]
        plt.savefig(os.path.join(output_folder_path, f"{fig_name}.png"),
                    dpi=config_plot.PLOT_SAVEFIG_DPI, bbox_inches="tight", facecolor=fig.get_facecolor())
        plt.close()
    else:
        plt.show()


def plot_corr_data(corr_data:List[np.ndarray[torch.Tensor]], labels:List[np.ndarray[torch.Tensor]], 
                    data_config:DatasetConfig, config_plot:PlotCorrConfig, corr_method:str, 
                    output_folder_path:str)->None:
    """
        - extract correlation data for each batch 
        - saves the corr data and its summary plot to output_folder_path
            ** if specidied in the config_plot saves seperatly for each marker 

        Args:
            corr_data: all samples correlation data.
            labels: corresponding labels
            data_config: config: with parameteres of the data. 
            config_plot: config: with parameteres of the plotting.
            output_folder_path: path to save the plots.

    """
    unique_batches = get_unique_parts_from_labels(labels[0], get_batches_from_labels, data_config)
    logging.info(f'[plot_corr_data] unique_batches: {unique_batches}')

    if data_config.SPLIT_DATA:
        data_set_types = ['trainset','valset','testset']
    else:
        data_set_types = ['testset']
    

    for i, set_type in enumerate(data_set_types):
        cur_corr_data, cur_labels = corr_data[i], labels[i]
        batch_of_label = get_batches_from_labels(cur_labels, data_config)
        __dict_temp = {batch: np.where(batch_of_label==batch)[0] for batch in unique_batches}
        logging.info(f'[plot_corr_data]: for set {set_type}, starting plotting {len(cur_labels)} samples.')

        for batch, batch_indexes in __dict_temp.items():
            batch_save_path = output_folder_path

            logging.info(f"[plot_corr_data] Saving {len(batch_indexes)} in {batch_save_path}")

            #extract current batch samples
            batch_corr_data = cur_corr_data[batch_indexes]
            batch_labels = cur_labels[batch_indexes]

            # extract current markers 
            batch_markers = np.array(get_markers_from_labels(batch_labels))
            marker_names = np.unique(batch_markers)

            # iterate each marker and plot/ save 
            corr_by_markers = {}
            for marker in marker_names:
                marker_save_path = os.path.join(batch_save_path, marker)
                os.makedirs(marker_save_path, exist_ok=True)
                indices_to_keep = (batch_markers == marker)
                marker_cor = batch_corr_data[indices_to_keep]
                logging.info(f"[plot_corr_data] Extracting {len(marker_cor)} samples of marker {marker}.")
                corr_by_markers[marker] = marker_cor

                # create correlation plots by seperate markers
                if config_plot.PLOT_CORR_SEPERATE_MARKERS:
                   plot_correlation(marker_cor, corr_method, config_plot, channel_names=['Nucleus', 'Marker'],  
                                                                sup_title = f"{marker}_{corr_method}_correlation", output_folder_path=marker_save_path, per_layer=config_plot.PLOT_CORR_PER_LAYER)
            
            # plot corr for all markers 
            if config_plot.PLOT_CORR_ALL_MARKERS:
                plot_correlation_by_markers(corr_by_markers, corr_method, config_plot, channel_names=['Nucleus', 'Marker'],  
                                                                        sup_title = f"{corr_method}_correlation", output_folder_path=batch_save_path, per_layer=config_plot.PLOT_CORR_PER_LAYER)
            
