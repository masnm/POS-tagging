from Word_Pos_List_Structure.Word_Pos_List_Structure import Word_POS_List
from CSV_File_To_List.CSV_File_To_List import CSV_File_To_List
from Tagset.Tagset import Tagset

class Conditional_Finder ( CSV_File_To_List ):

    conditional_lst_file = "src/CSV_files/conditional_list.csv"
    conditionals = []
    word_pos = []

    def __init__ ( self, word_pos:Word_POS_List ):
        self.word_pos = word_pos
        self.conditionals = self.file_to_list ( self.conditional_lst_file, "conditional" )
        self.mark_conditionals ()

    def mark_conditionals ( self ):
        for item in self.word_pos:
            for conditional in self.conditionals:
                if item.word == conditional:
                    item.pos_list.append ( Tagset.CND )

    def __repr__ ( self ):
        return str (
                # f"conditional {self.conditionals}\n"
                f"{self.word_pos}\n"
                )
