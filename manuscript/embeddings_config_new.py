import os
import sys
sys.path.insert(1, os.getenv("NOVA_HOME"))

from src.embeddings.embeddings_config import EmbeddingsConfig


################# Alyssa #######################

class EmbeddingsAlyssaCoyneDatasetConfig(EmbeddingsConfig):
    def __init__(self):
        super().__init__()

        self.INPUT_FOLDERS = [os.path.join(self.PROCESSED_FOLDER_ROOT, "ManuscriptFinalData_80pct", "AlyssaCoyne", f) for f in
                        ["batch1"]]
       
        self.SPLIT_DATA = False
        self.EXPERIMENT_TYPE = 'AlyssaCoyne'    
        self.MARKERS_TO_EXCLUDE = ['MERGED']
        self.ADD_BATCH_TO_LABEL = True
        self.ADD_REP_TO_LABEL = True

        self.SHUFFLE:bool = False

        self.SETS:List[str] = ['testset']

        self.MARKERS:List[str]            =  ["DAPI", "DCP1A", "Map2", "TDP43"]

        # Cell lines to include
        self.CELL_LINES:List[str]         = ["c9orf72ALSPatients", "sALSNegativeCytoTDP43", "sALSPositiveCytoTDP43", "Controls"]

        # Conditions to include
        self.CONDITIONS:List[str]         = ["Untreated"]


################# NEW dNLS #######################

class EmbeddingsNewdNLSDatasetConfig(EmbeddingsConfig):
    def __init__(self):
        super().__init__()

        self.INPUT_FOLDERS = None
       
        self.SPLIT_DATA = False
        self.EXPERIMENT_TYPE = 'dNLS'
        self.MARKERS_TO_EXCLUDE = []
        self.ADD_BATCH_TO_LABEL = True
        self.ADD_REP_TO_LABEL = True

class EmbeddingsNewdNLSCombinedDatasetConfig(EmbeddingsNewdNLSDatasetConfig):
    def __init__(self):
        super().__init__()

        self.INPUT_FOLDERS = [os.path.join(self.PROCESSED_FOLDER_ROOT, "ManuscriptFinalData_80pct", "dNLS", f) for f in
                        ["batch4", "batch5"]]

        self.SHUFFLE:bool = False

        self.SETS:List[str] = ['testset']

        self.MARKERS:List[str]            =  ["DCP1A", "TDP43", "LSM14A"]

        # Cell lines to include
        self.CELL_LINES:List[str]         = ["WT", "dNLS"]

        # Conditions to include
        self.CONDITIONS:List[str]         = ["dox", "Untreated"]


################# NEW INDI #######################
class EmbeddingsDay8NewDatasetConfig(EmbeddingsConfig):
    def __init__(self):
        super().__init__()

        self.INPUT_FOLDERS = None
       
        self.SPLIT_DATA = False
        self.EXPERIMENT_TYPE = 'neuronsDay8_new'
        self.MARKERS_TO_EXCLUDE = None
        self.ADD_BATCH_TO_LABEL = True
        self.ADD_REP_TO_LABEL = True



class EmbeddingsDay8CombinedDatasetConfig(EmbeddingsDay8NewDatasetConfig):
    def __init__(self):
        super().__init__()

        self.INPUT_FOLDERS = [os.path.join(self.PROCESSED_FOLDER_ROOT, "ManuscriptFinalData_80pct", "neuronsDay18", f) for f in
                        ["batch3", "batch8", "batch9"]]

        self.SHUFFLE:bool = False

        self.SETS:List[str] = ['testset']

        self.MARKERS:List[str]            =  ["G3BP1", "FUS", "FMRP", "TDP"]

        # Cell lines to include
        self.CELL_LINES:List[str]         = ["WT", "FUSHeterozygous", "FUSHomozygous", "FUSRevertant"]

        # Conditions to include
        self.CONDITIONS:List[str]         = ["stress", "Untreated"]