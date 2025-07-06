import sys
import os

sys.path.insert(1, os.getenv("NOVA_HOME"))

from abc import abstractmethod
import logging
import pandas as pd
import numpy as np
from typing import List, Tuple, Iterable, Dict
import itertools

from src.datasets.label_utils import get_unique_parts_from_labels, get_cell_lines_conditions_from_labels, get_markers_from_labels, get_batches_from_labels
from src.datasets.dataset_config import DatasetConfig
from src.analysis.analyzer import Analyzer
from src.common.utils import get_if_exists
from NOVA.src.datasets.label_utils import get_batches_from_labels, get_unique_parts_from_labels, get_markers_from_labels
from src.analysis.analyzer_pairwise_dist_utils import filter_by_labels, compute_distances, extract_pairs


class AnalyzerPairwiseDistances(Analyzer):
    """
    AnalyzerPairwiseDistances is responsible for calculating distances between t types of embedding conditions (for example: control vs. stress). 

    """
    def __init__(self, data_config: DatasetConfig, pairwise_config, output_folder_path:str):
        """Get an instance

        Args:
            data_config (DatasetConfig): The dataset configuration object. 
            output_folder_path (str): path to output folder
        """
        super().__init__(data_config, output_folder_path)
        self.pairwise_config = pairwise_config


    def calculate(self, embeddings:np.ndarray[float], labels:np.ndarray[str], paths: np.ndarray[str])->List[np.ndarray[torch.Tensor]]:
        """Calculate features from given embeddings, save in the self.features attribute and return them as well

        Args:
            embeddings (np.ndarray[float]): embedding vector for each sample
            labels (np.ndarray[str]): The corresponding labels of embeddings
            paths (np.ndarray[str]): The corresponding paths of embeddings
        Return:
            The calculated correlation data
        """
        raw_distances = {}
        pairs_df = {}
        marker_names = get_unique_parts_from_labels(labels, get_markers_from_labels, self.pairwise_config)
        for marker in marker_names:
                # filter by markers
                marker_labels, marker_embeddings, marker_paths = filter_by_labels(batch_labels, batch_embeddings, batch_paths, {"markers": marker})
                marker_distances, unique_conditions, filtered_paths_c1, filtered_paths_c2 = compute_distances(marker_embeddings, marker_labels, marker_paths, self.pairwise_config.metric)
                raw_distances[marker] = marker_distances

                distances_df = extract_pairs(distances, paths_c1, paths_c2, config, output_dir)
                pairs_df[marker] = distances_df
        
    def load(self) -> None:
        """
        Load the saved features, labels, and paths into the corresponding attributes.
        Stacks data per set into arrays with shape (num_sets, ...).
        """


        return None

    def save(self)->None:
        """"
        Save the calculated distances to a specified file.
        """

        return None

    @abstractmethod    
    def _compute_score(self, embeddings: np.ndarray[float], labels: np.ndarray[str]) -> Tuple[float,str]:
        """
        Abstract method to compute the score between two sets of embeddings.

        Args:
            embeddings (np.ndarray[float]): The embeddings to compute scores on.
            labels (np.ndarray[str]): Corresponding labels; should contain only 2 unique labels.

        Returns:
            float: The calculated score.
            str: Name of the score metric.
        """
        pass
    
    

    def _get_save_path(self, output_folder_path:str, file_type:str)->str: #TODO:ask sagy where to save
        
        savepath = os.path.join(output_folder_path, f"{file_type}.npy")
        return savepath

    