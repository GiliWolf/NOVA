import os
import sys
sys.path.insert(0, os.getenv("HOME"))
sys.path.insert(1, os.getenv("NOVA_HOME"))


import logging
from src.embeddings.embeddings_utils import load_embeddings
from src.common.utils import load_config_file
from src.datasets.dataset_config import DatasetConfig
from src.figures.plot_attention_config import PlotAttnMapConfig
from src.models.utils.consts import CHECKPOINT_BEST_FILENAME, CHECKPOINTS_FOLDERNAME
from typing import Dict, List, Optional, Tuple, Callable
from copy import deepcopy
import numpy as np
import torch
from src.figures.attention_maps_plotting import plot_attn_maps
from src.datasets.label_utils import get_batches_from_input_folders
from tools.load_data_from_npy import __extract_indices_to_plot, __extract_samples_to_plot
from src.analysis.analyzer_attention_correlation import AnalyzerAttnCorr


def load_and_plot_attn_maps(outputs_folder_path:str, config_path_data:str, config_path_plot:str):
    config_data:DatasetConfig = load_config_file(config_path_data, "data")
    config_data.OUTPUTS_FOLDER = outputs_folder_path
    config_plot:PlotAttnMapConfig = load_config_file(config_path_plot, "plot")
    corr_method = "pearsonr" # TODO: decide where to put corr_method
    # load processed attn maps
    processed_attn_maps, labels, paths = load_embeddings(os.path.join(outputs_folder_path, "attention_maps"), config_data, emb_folder_name = "processed")
    processed_attn_maps, labels, paths = [processed_attn_maps], [labels], [paths] #TODO: fix, needed for settypes
    
    
    # (!) TODO: create new attn plot config (without corr) - V 
    # (!) TODO: ceate attn_plot_utils if needed - X, in attention map plotting
    # (!) TODO: add flag to attn_plot config if to load corr_data (only if presented, add to figure) - V
    # (!) TODO: discard the need for config_attn in plot_attn_maps (use only plot  config) - V 
    # (!) TODO: save attn maps in figures directory - V
    # (!) TODO: make it work  - !!
    d = AnalyzerAttnCorr(config_data, output_folder_path, corr_method = corr_method) #TODO: decied if to instancize it - here only for the output dir

    # load correlation data if needed
    if config_plot.SHOW_CORR_SCORES:
        #corr_method = ????
        d.load()
        corr_data = d.features
    else:
        corr_method = ""
        corr_data = None

    # filter the subset if needed
    if config_plot.FILTER_SAMPLES_FOLDER_PATHS is not None:
            samples_indices = __extract_indices_to_plot(keep_samples_dirs=config_plot.FILTER_SAMPLES_FOLDER_PATHS, paths = paths, data_config = config_data)
            processed_attn_maps = __extract_samples_to_plot(processed_attn_maps, samples_indices, data_config = config_data)
            labels = __extract_samples_to_plot(labels, samples_indices, data_config = config_data)
            paths = __extract_samples_to_plot(paths, samples_indices, data_config = config_data)
            if corr_data is not None:
                corr_data = __extract_samples_to_plot(corr_data, samples_indices, data_config = config_data)

    # plot attn_maps (AFTER FILTERING)
    # TODO: keep seperation by settype?
    plot_attn_maps(processed_attn_maps, labels, paths, config_data, config_plot, output_folder_path=d.get_saving_folder(feature_type="attention_maps"),corr_data =  corr_data,corr_method = corr_method)


    
        

if __name__ == "__main__":
    print("Starting generating distances...")
    try:
        if len(sys.argv) < 4:
            raise ValueError("Invalid arguments. Must supply output folder path, data config and path config!")
        output_folder_path = sys.argv[1]
        config_path_data = sys.argv[2]
        config_path_plot = sys.argv[3]

        load_and_plot_attn_maps(output_folder_path, config_path_data, config_path_plot)
        
    except Exception as e:
        logging.exception(str(e))
        raise e
    logging.info("Done")
