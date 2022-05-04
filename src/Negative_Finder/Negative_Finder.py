from Word_Pos_List_Structure.Word_Pos_List_Structure import Word_POS_List
from CSV_File_To_List.CSV_File_To_List import CSV_File_To_List
from Tagset.Tagset import Tagset

class Negative_Finder ( CSV_File_To_List ):

    negative_lst_file = "src/CSV_files/negative_list.csv"
    negatives = []
    word_pos = []

    def __init__ ( self, word_pos:Word_POS_List ):
        self.word_pos = word_pos
        self.negatives = self.file_to_list ( self.negative_lst_file, "negative" )
        self.mark_negatives ()

    def mark_negatives ( self ):
        for item in self.word_pos:
            for negative in self.negatives:
                if item.word == negative:
                    item.pos_list.append ( Tagset.NEG )

    def __repr__ ( self ):
        return str (
                f"Negative {self.negatives}\n"
                f"{self.word_pos}\n"
                )
