import os
import sys

sys.path.insert(1, os.getenv("NOVA_HOME"))
print(f"NOVA_HOME: {os.getenv('NOVA_HOME')}")

import logging
from src.common.utils import load_config_file
from src.embeddings.embeddings_utils import load_embeddings
from src.datasets.dataset_config import DatasetConfig
from src.analysis.analyzer_attention_correlation import AnalyzerAttnCorr

def load_attn_and_plot_correlation(outputs_folder_path:str, config_path_data:str, config_path_plot:str = None):
    # TODO: check working, only calculating corrs
    config_data:DatasetConfig = load_config_file(config_path_data, "data")

    if config_path_plot:
        config_plot:PlotAttnMapConfig = load_config_file(config_path_plot, 'plot')
    config_data.OUTPUTS_FOLDER = outputs_folder_path

    # load processed attn maps
    processed_attn_maps, labels, paths = load_embeddings(os.path.join(outputs_folder_path, "attention_maps"), config_data, emb_folder_name = "processed")
    processed_attn_maps, labels, paths = [processed_attn_maps], [labels], [paths] #TODO: fix, needed for settypes
    
    logging.info("[Generate distances]")
    corr_method = "pearsonr"
    d = AnalyzerAttnCorr(config_data, output_folder_path, corr_method = corr_method)
    corr_data = d.calculate(processed_attn_maps, labels, paths)
    d.save()
        

if __name__ == "__main__":
    print("Starting generating distances...")
    try:
        if len(sys.argv) < 3:
            raise ValueError("Invalid arguments. Must supply output folder path and data config!")
        output_folder_path = sys.argv[1]
        config_path_data = sys.argv[2]

        if len(sys.argv) == 3:
            config_path_plot = sys.argv[3]
        else:
            config_path_plot = None
        load_attn_and_plot_correlation(output_folder_path, config_path_data)
        
    except Exception as e:
        logging.exception(str(e))
        raise e
    logging.info("Done")
