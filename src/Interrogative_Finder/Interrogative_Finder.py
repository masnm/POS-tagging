from Word_Pos_List_Structure.Word_Pos_List_Structure import Word_POS_List
from Tag_Using_Word_List.Tag_Using_Word_List import Tag_Using_Word_List
from CSV_File_To_List.CSV_File_To_List import CSV_File_To_List
from Tagset.Tagset import Tagset

class Interrogative_Finder ( CSV_File_To_List, Tag_Using_Word_List ):

    interrogative_lst_file = "src/CSV_files/interrogative_list.csv"
    interrogatives = []
    word_pos = []

    def __init__ ( self, word_pos:Word_POS_List ):
        self.word_pos = word_pos
        self.interrogatives = self.file_to_list ( self.interrogative_lst_file, "interrogative" )
        self.tag_using_word_list ( self.interrogatives, Tagset.ING )

    def __repr__ ( self ):
        return str (
                f"Interrogative {self.interrogatives}\n"
                f"{self.word_pos}\n"
                )
