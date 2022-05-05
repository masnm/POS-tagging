from Word_Pos_List_Structure.Word_Pos_List_Structure import Word_POS_List
from Tag_Using_Word_List.Tag_Using_Word_List import Tag_Using_Word_List
from CSV_File_To_List.CSV_File_To_List import CSV_File_To_List
from Tagset.Tagset import Tagset

class Conditional_Finder ( CSV_File_To_List, Tag_Using_Word_List ):

    conditional_lst_file = "src/CSV_files/conditional_list.csv"
    conditionals = []
    word_pos = []

    def __init__ ( self, word_pos:Word_POS_List ):
        self.word_pos = word_pos
        self.conditionals = self.file_to_list ( self.conditional_lst_file, "conditional" )
        self.tag_using_word_list ( self.conditionals, Tagset.CND )

    def __repr__ ( self ):
        return str (
                # f"conditional {self.conditionals}\n"
                f"{self.word_pos}\n"
                )
