from Word_Pos_List_Structure.Word_Pos_List_Structure import Word_POS_List
from Tag_Using_Word_List.Tag_Using_Word_List import Tag_Using_Word_List
from CSV_File_To_List.CSV_File_To_List import CSV_File_To_List
from Tagset.Tagset import Tagset

class Adjective_Of_Adjective_Finder ( CSV_File_To_List, Tag_Using_Word_List ):

    adjective_of_adjective_lst_file = "src/CSV_files/adjectiv_of_adjective_list.csv"
    adjective_of_adjectives = []
    word_pos = []

    def __init__ ( self, word_pos:Word_POS_List ):
        self.word_pos = word_pos
        self.adjective_of_adjectives = self.file_to_list ( self.adjective_of_adjective_lst_file, "adjective of adjective" )
        self.tag_using_word_list ( self.adjective_of_adjectives, Tagset.ADA )

    def __repr__ ( self ):
        ret:str = "";
        ret += f"Adjective Of Adjective : {len(self.adjective_of_adjectives)}\n"
        for wp in self.word_pos:
            ret += f"{wp}\n"
        return ret;
