import os
import sys
sys.path.insert(1, os.getenv("NOVA_HOME"))
from typing import List
from src.embeddings.embeddings_config import EmbeddingsConfig


################# Micheal Ward (NIH) #######################
class EmbeddingsNIHDatasetConfig(EmbeddingsConfig):
    def __init__(self):
        super().__init__()

        self.INPUT_FOLDERS = None
       
        self.SPLIT_DATA = False
        self.EXPERIMENT_TYPE = 'NIH'
        self.MARKERS_TO_EXCLUDE = None
        self.ADD_BATCH_TO_LABEL = True
        self.ADD_REP_TO_LABEL = True
        self.SHUFFLE:bool = False
        self.SETS:List[str] = ['testset']
        



# class EmbeddingsNIHDatasetConfigCombined(EmbeddingsNIHDatasetConfig):
#     def __init__(self):
#         super().__init__()

#         # Conditions to include
#         self.CONDITIONS:List[str]         = ["stress", "Untreated"]

#         self.CELL_LINES:List[str]         = ["WT"]

#         self.MARKERS:List[str]            =  [ "PML", "TOMM20", "PURA", "DCP1A", "TUJ1", "TDP43"] #["G3BP1", "FMRP",mitotracker]


class newNeuronsD8FigureConfig_G3BP1_FMRP_stress_All(EmbeddingsNIHDatasetConfig):
    def __init__(self):
        super().__init__()
       
        self.EXPERIMENT_TYPE = 'NIH'    
        self.CELL_LINES = ['WT']
        self.CONDITIONS = ['stress', 'Untreated'] # vs each other
        self.MARKERS = ['G3BP1', 'FMRP']


class newNeuronsD8FigureConfig_G3BP1_FMRP_stress_Batch1(newNeuronsD8FigureConfig_G3BP1_FMRP_stress_All):
    def __init__(self):
        super().__init__()
                
        self.INPUT_FOLDERS = [os.path.join(self.PROCESSED_FOLDER_ROOT, "ManuscriptFinalData_80pct", "NIH", f) for f in
                        ["batch1"]]

class newNeuronsD8FigureConfig_G3BP1_FMRP_stress_Batch2(newNeuronsD8FigureConfig_G3BP1_FMRP_stress_All):
    def __init__(self):
        super().__init__()
                
        self.INPUT_FOLDERS = [os.path.join(self.PROCESSED_FOLDER_ROOT, "ManuscriptFinalData_80pct", "NIH", f) for f in
                        ["batch2"]]

class newNeuronsD8FigureConfig_G3BP1_FMRP_stress_Batch3(newNeuronsD8FigureConfig_G3BP1_FMRP_stress_All):
    def __init__(self):
        super().__init__()
                
        self.INPUT_FOLDERS = [os.path.join(self.PROCESSED_FOLDER_ROOT, "ManuscriptFinalData_80pct", "NIH", f) for f in
                        ["batch3"]]
        
class newNeuronsD8FigureConfig_G3BP1_FMRP_stress_Batch1Subset(newNeuronsD8FigureConfig_G3BP1_FMRP_stress_Batch1):
    def __init__(self):
        super().__init__()
                

class newNeuronsD8FigureConfig_G3BP1_FMRP_stress_Batch2Subset(newNeuronsD8FigureConfig_G3BP1_FMRP_stress_Batch2):
    def __init__(self):
        super().__init__()
                

class newNeuronsD8FigureConfig_G3BP1_FMRP_stress_Batch3Subset(newNeuronsD8FigureConfig_G3BP1_FMRP_stress_Batch3):
    def __init__(self):
        super().__init__()
                


# class EmbeddingsNIHDatasetConfigBatch1(EmbeddingsNIHDatasetConfigCombined):
#     def __init__(self):
#         super().__init__()

#         self.INPUT_FOLDERS = [os.path.join(self.PROCESSED_FOLDER_ROOT, "ManuscriptFinalData_80pct", "NIH", f) for f in
#                         ["batch1"]]
# class NIHWTStressvsUntreatedBatch1Subset(EmbeddingsNIHDatasetConfigBatch1):
#     def __init__(self):
#         super().__init__()


# class EmbeddingsNIHDatasetConfigBatch2(EmbeddingsNIHDatasetConfigCombined):
#     def __init__(self):
#         super().__init__()

#         self.INPUT_FOLDERS = [os.path.join(self.PROCESSED_FOLDER_ROOT, "ManuscriptFinalData_80pct", "NIH", f) for f in
#                         ["batch2"]]

# class NIHWTStressvsUntreatedBatch2Subset(EmbeddingsNIHDatasetConfigBatch2):
#     def __init__(self):
#         super().__init__()

# class EmbeddingsNIHDatasetConfigBatch3(EmbeddingsNIHDatasetConfigCombined):
#     def __init__(self):
#         super().__init__()

#         self.INPUT_FOLDERS = [os.path.join(self.PROCESSED_FOLDER_ROOT, "ManuscriptFinalData_80pct", "NIH", f) for f in
#                         ["batch3"]]

# class NIHWTStressvsUntreatedBatch3Subset(EmbeddingsNIHDatasetConfigBatch3):
#     def __init__(self):
#         super().__init__()