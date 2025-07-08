import os
import sys
sys.path.insert(1, os.getenv("NOVA_HOME"))

from src.embeddings.embeddings_config import EmbeddingsConfig


################# Alyssa: EmbeddingsAlyssaCoyneDatasetConfig #######################

class EmbeddingsAlyssaCoyneDatasetConfig(EmbeddingsConfig):
    def __init__(self):
        super().__init__()
        
        self.INPUT_FOLDERS = None
        self.SPLIT_DATA = False
        self.EXPERIMENT_TYPE = 'AlyssaCoyne'    
        self.MARKERS_TO_EXCLUDE = ['MERGED']
        self.ADD_BATCH_TO_LABEL = True
        self.ADD_REP_TO_LABEL = True

        self.SHUFFLE:bool = False

        self.SETS:List[str] = ['testset']


class EmbeddingsAlyssaCoyneDatasetConfigCombined(EmbeddingsAlyssaCoyneDatasetConfig):
    def __init__(self):
        super().__init__()

        self.INPUT_FOLDERS = [os.path.join(self.PROCESSED_FOLDER_ROOT, "ManuscriptFinalData_80pct", "AlyssaCoyne", f) for f in
                        ["batch1"]]
       

        self.MARKERS:List[str]            =  ["DAPI", "DCP1A", "Map2", "TDP43"]

        # Cell lines to include
        self.CELL_LINES:List[str]         = ["c9orf72ALSPatients", "sALSNegativeCytoTDP43", "sALSPositiveCytoTDP43", "Controls"]

        # Conditions to include
        self.CONDITIONS:List[str]         = ["Untreated"]

## SUBSET CONFIGS:
class AlyssaCoyneC9vsControlSubset(EmbeddingsAlyssaCoyneDatasetConfigCombined):

    def __init__(self):
        super().__init__()

        # Cell lines to include
        self.CELL_LINES:List[str]         = ["c9orf72ALSPatients", "Controls"]

        # Conditions to include
        self.CONDITIONS:List[str]         = ["Untreated"]

class AlyssaCoyneNegativeTDP43vsControlSubset(EmbeddingsAlyssaCoyneDatasetConfigCombined):
    def __init__(self):
        super().__init__()

        self.CELL_LINES: List[str] = ["sALSNegativeCytoTDP43", "Controls"]
        self.CONDITIONS: List[str] = ["Untreated"]

class AlyssaCoynePositiveTDP43vsControlSubset(EmbeddingsAlyssaCoyneDatasetConfigCombined):
    def __init__(self):
        super().__init__()

        self.CELL_LINES: List[str] = ["sALSPositiveCytoTDP43", "Controls"]
        self.CONDITIONS: List[str] = ["Untreated"]

################# NEW dNLS: EmbeddingsNewdNLSCombinedDatasetConfig #######################

class EmbeddingsNewdNLSDatasetConfig(EmbeddingsConfig):
    def __init__(self):
        super().__init__()

        self.INPUT_FOLDERS = None
       
        self.SPLIT_DATA = False
        self.EXPERIMENT_TYPE = 'dNLS'
        self.MARKERS_TO_EXCLUDE = []
        self.ADD_BATCH_TO_LABEL = True
        self.ADD_REP_TO_LABEL = True

class EmbeddingsNewdNLSDatasetConfigCombined(EmbeddingsNewdNLSDatasetConfig):
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

# SUBSET 
class NewdNLSDoxVsUntreatedSubset(EmbeddingsNewdNLSDatasetConfigCombined):
    def __init__(self):
        super().__init__()

        self.CELL_LINES: List[str] = ["dNLS"]
        self.CONDITIONS: List[str] = ["dox", "untreated"]

################# NEW INDI: EmbeddingsDay8CombinedDatasetConfig #######################
class EmbeddingsDay8NewDatasetConfig(EmbeddingsConfig):
    def __init__(self):
        super().__init__()

        self.INPUT_FOLDERS = None
       
        self.SPLIT_DATA = False
        self.EXPERIMENT_TYPE = 'neuronsDay8_new'
        self.MARKERS_TO_EXCLUDE = None
        self.ADD_BATCH_TO_LABEL = True
        self.ADD_REP_TO_LABEL = True



class EmbeddingsDay8DatasetConfigCombined(EmbeddingsDay8NewDatasetConfig):
    def __init__(self):
        super().__init__()

        self.INPUT_FOLDERS = [os.path.join(self.PROCESSED_FOLDER_ROOT, "ManuscriptFinalData_80pct", "neuronsDay8_new", f) for f in
                        ["batch8"]]

        self.SHUFFLE:bool = False

        self.SETS:List[str] = ['testset']

        self.MARKERS:List[str]            =  ["G3BP1", "FUS", "FMRP", "TDP"]

        # Cell lines to include
        self.CELL_LINES:List[str]         = ["WT", "FUSHeterozygous", "FUSHomozygous", "FUSRevertant"]

        # Conditions to include
        self.CONDITIONS:List[str]         = ["stress", "Untreated"]


class NewIndiFUSHeteroVsRevertantSubset(EmbeddingsDay8DatasetConfigCombined):
    def __init__(self):
        super().__init__()

        self.CELL_LINES: List[str] = ["FUSHeterozygous", "FUSRevertant"]
        self.CONDITIONS: List[str] = ["Untreated"]
        self.MARKERS: List[str] = ["FUS"]


class NewIndiFUSHeteroVsWTSubset(EmbeddingsDay8DatasetConfigCombined):
    def __init__(self):
        super().__init__()

        self.CELL_LINES: List[str] = ["FUSHeterozygous", "WT"]
        self.CONDITIONS: List[str] = ["Untreated"]
        self.MARKERS: List[str] = ["FUS"]

class NewIndiFUSHomoVsRevertantSubset(EmbeddingsDay8DatasetConfigCombined):
    def __init__(self):
        super().__init__()

        self.CELL_LINES: List[str] = ["FUSHomozygous", "FUSRevertant"]
        self.CONDITIONS: List[str] = ["Untreated"]
        self.MARKERS: List[str] = ["FUS"]

class NewIndiFUSHomoVsWTSubset(EmbeddingsDay8DatasetConfigCombined):
    def __init__(self):
        super().__init__()

        self.CELL_LINES: List[str] = ["FUSHomozygous", "WT"]
        self.CONDITIONS: List[str] = ["Untreated"]
        self.MARKERS: List[str] = ["FUS"]

class NewIndiFUSHeteroVsHomoSubset(EmbeddingsDay8DatasetConfigCombined):
    def __init__(self):
        super().__init__()

        self.CELL_LINES: List[str] = ["FUSHeterozygous", "FUSHomozygous"]
        self.CONDITIONS: List[str] = ["Untreated"]
        self.MARKERS: List[str] = ["FUS"]

class NewIndiTDP43vsWTSubset(EmbeddingsDay8DatasetConfigCombined):
    def __init__(self):
        super().__init__()

        self.CELL_LINES: List[str] = ["TDP43", "WT"]
        self.CONDITIONS: List[str] = ["Untreated"]
        self.MARKERS: List[str] = ["TDP"]

class NewIndiWTStressVsUntreatedSubset(EmbeddingsDay8DatasetConfigCombined):
    def __init__(self):
        super().__init__()

        self.CELL_LINES: List[str] = ["WT"]
        self.CONDITIONS: List[str] = ["stress", "Untreated"]
        self.MARKERS: List[str] = ["G3BP1", "FMRP"]