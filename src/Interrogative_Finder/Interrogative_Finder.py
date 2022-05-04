from Word_Pos_List_Structure.Word_Pos_List_Structure import Word_POS_List
from CSV_File_To_List.CSV_File_To_List import CSV_File_To_List
from Tagset.Tagset import Tagset

class Interrogative_Finder ( CSV_File_To_List ):

    interrogative_lst_file = "src/CSV_files/interrogative_list.csv"
    interrogatives = []
    word_pos = []

    def __init__ ( self, word_pos:Word_POS_List ):
        self.word_pos = word_pos
        self.interrogatives = self.file_to_list ( self.interrogative_lst_file, "interrogative" )
        self.mark_interrogatives ()

    def mark_interrogatives ( self ):
        for item in self.word_pos:
            for interrogative in self.interrogatives:
                if item.word == interrogative:
                    item.pos_list.append ( Tagset.ING )

    def __repr__ ( self ):
        return str (
                f"Interrogative {self.interrogatives}\n"
                f"{self.word_pos}\n"
                )
