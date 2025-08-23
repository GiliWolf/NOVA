######################################################
########## Please Don't Change This Section ##########
######################################################

import os
import sys

sys.path.insert(1, os.getenv("NOVA_HOME"))
from tools.images_organizer.opera_version2.config import Config


class Config_A1(Config):
    def __init__(self):
        super().__init__()

        # folder_name = "PanelABC_Batch1"
        folder_name = "batch1"
        self.FOLDERS = [folder_name]
        # self.INCLUDE_SUB_FOLDERS = [f'{folder_name}/images']
        self.INCLUDE_SUB_FOLDERS = [f'{folder_name}/PanelA']



        ##################################

        ########################################
        ############### Advanced ###############
        ########################################
        row_rep1 = 1
        row_rep2 = 2
        row_rep3 = 3
        row_rep4 = 4
        row_rep5 = 5
        row_rep6 = 6
        row_rep7 = 7
        row_rep8 = 8
        self.CONFIG = {
            self.KEY_CELL_LINES: {
                "WT": {
                    "stress": [(row_rep5,1), (row_rep6,1), (row_rep7,1), (row_rep8,1)], 
                    "Untreated": [(row_rep1,1), (row_rep2,1), (row_rep3,1), (row_rep4,1)]
                },
        
            },
            # [DAPI, mCherry, GFP, Cy5]
            # ch01 - DAPI
            # ch02 - Cy3 (mCherry)
            # ch03 - Cy2 (GFP)
            # ch04 - Cy5
            self.KEY_MARKERS_ALIAS_ORDERED: ["ch1", "ch2"],
            self.KEY_MARKERS: {
                'panelA': ["DAPI", "DCP1A"]
                },
            self.KEY_REPS: ["rep1", "rep2","rep3","rep4","rep5", "rep6","rep7","rep8"],
        }

#######################################

class Config_A2(Config):
    def __init__(self):
        super().__init__()

        # folder_name = "PanelABC_Batch1"
        folder_name = 'batch2'
        self.FOLDERS = [folder_name]
        # self.INCLUDE_SUB_FOLDERS = [f'{folder_name}/images']
        self.INCLUDE_SUB_FOLDERS = [f'{folder_name}/PanelA']



        ##################################

        ########################################
        ############### Advanced ###############
        ########################################
        row_rep1 = 1
        row_rep2 = 2
        row_rep3 = 3
        row_rep4 = 4
        row_rep5 = 5
        row_rep6 = 6
        row_rep7 = 7
        row_rep8 = 8
        self.CONFIG = {
            self.KEY_CELL_LINES: {
                "WT": {
                    "stress": [(row_rep5,5), (row_rep6,5), (row_rep7,5), (row_rep8,5)], 
                    "Untreated": [(row_rep1,5), (row_rep2,5), (row_rep3,5), (row_rep4,5)]
                },
        
            },
            # [DAPI, mCherry, GFP, Cy5]
            # ch01 - DAPI
            # ch02 - Cy3 (mCherry)
            # ch03 - Cy2 (GFP)
            # ch04 - Cy5
            self.KEY_MARKERS_ALIAS_ORDERED: ["ch1", "ch2"],
            self.KEY_MARKERS: {
                'panelA': ["DAPI", "DCP1A"]
                },
            self.KEY_REPS: ["rep1", "rep2","rep3","rep4","rep5", "rep6","rep7","rep8"],
        }

#######################################

class Config_A3(Config):
    def __init__(self):
        super().__init__()

        # folder_name = "PanelABC_Batch1"
        folder_name = 'batch3'
        self.FOLDERS = [folder_name]
        # self.INCLUDE_SUB_FOLDERS = [f'{folder_name}/images']
        self.INCLUDE_SUB_FOLDERS = [f'{folder_name}/PanelA']



        ##################################

        ########################################
        ############### Advanced ###############
        ########################################
        row_rep1 = 1
        row_rep2 = 2
        row_rep3 = 3
        row_rep4 = 4
        row_rep5 = 5
        row_rep6 = 6
        row_rep7 = 7
        row_rep8 = 8
        self.CONFIG = {
            self.KEY_CELL_LINES: {
                "WT": {
                    "stress": [(row_rep5,9), (row_rep6,9), (row_rep7,9), (row_rep8,9)], 
                    "Untreated": [(row_rep1,9), (row_rep2,9), (row_rep3,9), (row_rep4,9)]
                },
        
            },
            # [DAPI, mCherry, GFP, Cy5]
            # ch01 - DAPI
            # ch02 - Cy3 (mCherry)
            # ch03 - Cy2 (GFP)
            # ch04 - Cy5
            self.KEY_MARKERS_ALIAS_ORDERED: ["ch1", "ch2"],
            self.KEY_MARKERS: {
                'panelA': ["DAPI", "DCP1A"]
                },
            self.KEY_REPS: ["rep1", "rep2","rep3","rep4","rep5", "rep6","rep7","rep8"],
        }

#######################################


class Config_B1(Config):
    def __init__(self):
        super().__init__()

        folder_name = 'batch1'
        self.FOLDERS = [folder_name]
        self.INCLUDE_SUB_FOLDERS = [f'{folder_name}/PanelB']



        ##################################

        ########################################
        ############### Advanced ###############
        ########################################
        row_rep1 = 1
        row_rep2 = 2
        row_rep3 = 3
        row_rep4 = 4
        row_rep5 = 5
        row_rep6 = 6
        row_rep7 = 7
        row_rep8 = 8
        
        self.CONFIG = {
            self.KEY_CELL_LINES: {
                "WT": {
                    "stress": [(row_rep5,2), (row_rep6,2), (row_rep7,2), (row_rep8,2)], 
                    "Untreated": [(row_rep1,2), (row_rep2,2), (row_rep3,2), (row_rep4,2)]
                },
            },
            # [DAPI, mCherry, GFP, Cy5]
            # ch01 - DAPI
            # ch02 - Cy3 (mCherry)
            # ch03 - Cy2 (GFP)
            # ch04 - Cy5
            self.KEY_MARKERS_ALIAS_ORDERED: ["ch1", "ch2"],
            self.KEY_MARKERS: {
                'panelB': ["DAPI", "LSM14A"]
                },
            self.KEY_REPS: ["rep1", "rep2","rep3","rep4","rep5", "rep6","rep7","rep8"],
        }

#######################################

class Config_B2(Config):
    def __init__(self):
        super().__init__()

        folder_name = 'batch2'
        self.FOLDERS = [folder_name]
        self.INCLUDE_SUB_FOLDERS = [f'{folder_name}/PanelB']



        ##################################

        ########################################
        ############### Advanced ###############
        ########################################
        row_rep1 = 1
        row_rep2 = 2
        row_rep3 = 3
        row_rep4 = 4
        row_rep5 = 5
        row_rep6 = 6
        row_rep7 = 7
        row_rep8 = 8
        
        self.CONFIG = {
            self.KEY_CELL_LINES: {
                "WT": {
                    "stress": [(row_rep5,6), (row_rep6,6), (row_rep7,6), (row_rep8,6)], 
                    "Untreated": [(row_rep1,6), (row_rep2,6), (row_rep3,6), (row_rep4,6)]
                },
            },
            # [DAPI, mCherry, GFP, Cy5]
            # ch01 - DAPI
            # ch02 - Cy3 (mCherry)
            # ch03 - Cy2 (GFP)
            # ch04 - Cy5
            self.KEY_MARKERS_ALIAS_ORDERED: ["ch1", "ch2"],
            self.KEY_MARKERS: {
                'panelB': ["DAPI", "LSM14A"]
                },
            self.KEY_REPS: ["rep1", "rep2","rep3","rep4","rep5", "rep6","rep7","rep8"],
        }

#######################################


class Config_B3(Config):
    def __init__(self):
        super().__init__()

        folder_name = "batch3"
        self.FOLDERS = [folder_name]
        self.INCLUDE_SUB_FOLDERS = [f'{folder_name}/PanelB']



        ##################################

        ########################################
        ############### Advanced ###############
        ########################################
        row_rep1 = 1
        row_rep2 = 2
        row_rep3 = 3
        row_rep4 = 4
        row_rep5 = 5
        row_rep6 = 6
        row_rep7 = 7
        row_rep8 = 8
        
        self.CONFIG = {
            self.KEY_CELL_LINES: {
                "WT": {
                    "stress": [(row_rep5,10), (row_rep6,10), (row_rep7,10), (row_rep8,10)], 
                    "Untreated": [(row_rep1,10), (row_rep2,10), (row_rep3,10), (row_rep4,10)]
                },
            },
            # [DAPI, mCherry, GFP, Cy5]
            # ch01 - DAPI
            # ch02 - Cy3 (mCherry)
            # ch03 - Cy2 (GFP)
            # ch04 - Cy5
            self.KEY_MARKERS_ALIAS_ORDERED: ["ch1", "ch2"],
            self.KEY_MARKERS: {
                'panelB': ["DAPI", "LSM14A"]
                },
            self.KEY_REPS: ["rep1", "rep2","rep3","rep4","rep5", "rep6","rep7","rep8"],
        }

#######################################

class Config_C1(Config):
    def __init__(self):
        super().__init__()

        folder_name = 'batch1'
        self.FOLDERS = [folder_name]
        self.INCLUDE_SUB_FOLDERS = [f'{folder_name}/PanelC']



        ##################################

        ########################################
        ############### Advanced ###############
        ########################################
        
        row_rep1 = 1
        row_rep2 = 2
        row_rep3 = 3
        row_rep4 = 4
        row_rep5 = 5
        row_rep6 = 6
        row_rep7 = 7
        row_rep8 = 8
        
        self.CONFIG = {
            self.KEY_CELL_LINES: {
                "WT": {
                    "stress": [(row_rep5,3), (row_rep6,3), (row_rep7,3), (row_rep8,3)], 
                    "Untreated": [(row_rep1,3), (row_rep2,3), (row_rep3,3), (row_rep4,3)]
                },
            },
            # [DAPI, mCherry, GFP, Cy5]
            # ch01 - DAPI
            # ch02 - Cy3 (mCherry)
            # ch03 - Cy2 (GFP)
            # ch04 - Cy5
            self.KEY_MARKERS_ALIAS_ORDERED: ["ch1", "ch2"],
            self.KEY_MARKERS: {
                'panelC': ["DAPI", "TDP43"]
                },
            self.KEY_REPS: ["rep1", "rep2","rep3","rep4","rep5", "rep6","rep7","rep8"],
        }

#######################################

class Config_C2(Config):
    def __init__(self):
        super().__init__()

        folder_name = 'batch2'
        self.FOLDERS = [folder_name]
        self.INCLUDE_SUB_FOLDERS = [f'{folder_name}/PanelC']



        ##################################

        ########################################
        ############### Advanced ###############
        ########################################
        
        row_rep1 = 1
        row_rep2 = 2
        row_rep3 = 3
        row_rep4 = 4
        row_rep5 = 5
        row_rep6 = 6
        row_rep7 = 7
        row_rep8 = 8
        
        self.CONFIG = {
            self.KEY_CELL_LINES: {
                "WT": {
                    "stress": [(row_rep5,7), (row_rep6,7), (row_rep7,7), (row_rep8,7)], 
                    "Untreated": [(row_rep1,7), (row_rep2,7), (row_rep3,7), (row_rep4,7)]
                },
            },
            # [DAPI, mCherry, GFP, Cy5]
            # ch01 - DAPI
            # ch02 - Cy3 (mCherry)
            # ch03 - Cy2 (GFP)
            # ch04 - Cy5
            self.KEY_MARKERS_ALIAS_ORDERED: ["ch1", "ch2"],
            self.KEY_MARKERS: {
                'panelC': ["DAPI", "TDP43"]
                },
            self.KEY_REPS: ["rep1", "rep2","rep3","rep4","rep5", "rep6","rep7","rep8"],
        }

#######################################

class Config_C3(Config):
    def __init__(self):
        super().__init__()

        folder_name = 'batch3'
        self.FOLDERS = [folder_name]
        self.INCLUDE_SUB_FOLDERS = [f'{folder_name}/PanelC']



        ##################################

        ########################################
        ############### Advanced ###############
        ########################################
        
        row_rep1 = 1
        row_rep2 = 2
        row_rep3 = 3
        row_rep4 = 4
        row_rep5 = 5
        row_rep6 = 6
        row_rep7 = 7
        row_rep8 = 8
        
        self.CONFIG = {
            self.KEY_CELL_LINES: {
                "WT": {
                    "stress": [(row_rep5,11), (row_rep6,11), (row_rep7,11), (row_rep8,11)], 
                    "Untreated": [(row_rep1,11), (row_rep2,11), (row_rep3,11), (row_rep4,11)]
                },
            },
            # [DAPI, mCherry, GFP, Cy5]
            # ch01 - DAPI
            # ch02 - Cy3 (mCherry)
            # ch03 - Cy2 (GFP)
            # ch04 - Cy5
            self.KEY_MARKERS_ALIAS_ORDERED: ["ch1", "ch2"],
            self.KEY_MARKERS: {
                'panelC': ["DAPI", "TDP43"]
                },
            self.KEY_REPS: ["rep1", "rep2","rep3","rep4","rep5", "rep6","rep7","rep8"],
        }

#######################################



class Config_D1(Config):
    def __init__(self):
        super().__init__()

        folder_name = 'batch1'
        self.FOLDERS = [folder_name]
        self.INCLUDE_SUB_FOLDERS = [f'{folder_name}/PanelD']



        ##################################

        ########################################
        ############### Advanced ###############
        ########################################
        row_rep1 = 1
        row_rep2 = 2
        row_rep3 = 3
        row_rep4 = 4
        row_rep5 = 5
        row_rep6 = 6
        row_rep7 = 7
        row_rep8 = 8
        
        
        self.CONFIG = {
            self.KEY_CELL_LINES: {
                "WT": {
                    "stress": [(row_rep5,4), (row_rep6,4), (row_rep7,4), (row_rep8,4)], 
                    "Untreated": [(row_rep1,4), (row_rep2,4), (row_rep3,4), (row_rep4,4)]
                },

            },
            # [DAPI, Cy5, mCherry]
            # ch01 - DAPI
            # ch02 - Cy5
            # ch03 - Cy3 (mCherry)
            self.KEY_MARKERS_ALIAS_ORDERED: ["ch1", "ch2","ch3"],
            self.KEY_MARKERS: {
                'panelD': ["DAPI", "TDP43", "DCP1A"]
                },
            self.KEY_REPS: ["rep1", "rep2","rep3","rep4","rep5", "rep6","rep7","rep8"],
        }

#######################################

class Config_D2(Config):
    def __init__(self):
        super().__init__()

        folder_name = 'batch2'
        self.FOLDERS = [folder_name]
        self.INCLUDE_SUB_FOLDERS = [f'{folder_name}/PanelD']



        ##################################

        ########################################
        ############### Advanced ###############
        ########################################
        row_rep1 = 1
        row_rep2 = 2
        row_rep3 = 3
        row_rep4 = 4
        row_rep5 = 5
        row_rep6 = 6
        row_rep7 = 7
        row_rep8 = 8
        
        
        self.CONFIG = {
            self.KEY_CELL_LINES: {
                "WT": {
                    "stress": [(row_rep5,8), (row_rep6,8), (row_rep7,8), (row_rep8,8)], 
                    "Untreated": [(row_rep1,8), (row_rep2,8), (row_rep3,8), (row_rep4,8)]
                },

            },
            # [DAPI, Cy5, mCherry]
            # ch01 - DAPI
            # ch02 - Cy5
            # ch03 - Cy3 (mCherry)
            self.KEY_MARKERS_ALIAS_ORDERED: ["ch1", "ch2","ch3"],
            self.KEY_MARKERS: {
                'panelD': ["DAPI", "TDP43", "DCP1A"]
                },
            self.KEY_REPS: ["rep1", "rep2","rep3","rep4","rep5", "rep6","rep7","rep8"],
        }

#######################################

class Config_D3(Config):
    def __init__(self):
        super().__init__()

        folder_name = 'batch3'
        self.FOLDERS = [folder_name]
        self.INCLUDE_SUB_FOLDERS = [f'{folder_name}/PanelD']



        ##################################

        ########################################
        ############### Advanced ###############
        ########################################
        row_rep1 = 1
        row_rep2 = 2
        row_rep3 = 3
        row_rep4 = 4
        row_rep5 = 5
        row_rep6 = 6
        row_rep7 = 7
        row_rep8 = 8
        
        
        self.CONFIG = {
            self.KEY_CELL_LINES: {
                "WT": {
                    "stress": [(row_rep5,12), (row_rep6,12), (row_rep7,12), (row_rep8,12)], 
                    "Untreated": [(row_rep1,12), (row_rep2,12), (row_rep3,12), (row_rep4,12)]
                },

            },
            # [DAPI, Cy5, mCherry]
            # ch01 - DAPI
            # ch02 - Cy5
            # ch03 - Cy3 (mCherry)
            self.KEY_MARKERS_ALIAS_ORDERED: ["ch1", "ch2","ch3"],
            self.KEY_MARKERS: {
                'panelD': ["DAPI", "TDP43", "DCP1A"]
                },
            self.KEY_REPS: ["rep1", "rep2","rep3","rep4","rep5", "rep6","rep7","rep8"],
        }

#######################################
