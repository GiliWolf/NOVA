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
from src.analysis.analyzer_correlation_utils import *


class AnalyzerAttnCorr(Analyzer):
    """
    AnalyzerAttnCorr is responsible for calculating correlation scores between attention maps and their corresponding input images. 
    The correlation scores are computed for each marker and batch.
    """
    def __init__(self, data_config: DatasetConfig, output_folder_path:str, corr_method:str):
        """Get an instance

        Args:
            data_config (DatasetConfig): The dataset configuration object. 
            output_folder_path (str): path to output folder
        """
        super().__init__(data_config, output_folder_path)
        self.corr_method = corr_method

    def calculate(self, processed_attn_maps:np.ndarray[float], labels:np.ndarray[str], paths: np.ndarray[str])->List[np.ndarray[torch.Tensor]]:
        """Calculate features from given embeddings, save in the self.features attribute and return them as well

        Args:
            processed_attn_maps (np.ndarray[float]): The processed attention maps, already in the img shape (H,W)
            labels (np.ndarray[str]): The corresponding labels of attention maps
            paths (np.ndarray[str]): The corresponding paths of attention maps
        Return:
            The calculated correlation data
        """
        corr_data = compute_attn_correlations(processed_attn_maps, labels, paths, data_config = self.data_config, corr_method = self.corr_method)
        return corr_data
    
    def load(self)->None:
        """load the saved features into the self.features attribute
        """
        output_folder_path = self.get_saving_folder(feature_type='attn_correlations')
        logging.info(f"[save scores]: output_folder_path: {output_folder_path}")
        loadpath = self._get_save_path(output_folder_path)
        self.features = np.load(loadpath)
        return None

    def save(self)->None:
        """"
        Save the calculated distances to a specified file.
        """
        output_folder_path = self.get_saving_folder(feature_type='attn_correlations')
        os.makedirs(output_folder_path, exist_ok=True)
        savepath = self._get_save_path(output_folder_path)
        logging.info(f"Saving scores to {savepath}")
        np.save(savepath, self.features)
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

    def _get_save_path(self, output_folder_path:str)->str: #TODO:ask sagy where to save
        
        savepath = os.path.join(output_folder_path, "corrs.npy")
        return savepath

    