from Word_Pos_List_Structure.Word_Pos_List_Structure import Word_POS_List
from Tag_Using_Word_List.Tag_Using_Word_List import Tag_Using_Word_List
from CSV_File_To_List.CSV_File_To_List import CSV_File_To_List
from Tagset.Tagset import Tagset

class Degree_Finder ( CSV_File_To_List, Tag_Using_Word_List ):

    degree_lst_file = "src/CSV_files/degree_list.csv"
    degrees = []
    word_pos = []

    def __init__ ( self, word_pos:Word_POS_List ):
        self.word_pos = word_pos
        self.degrees = self.file_to_list ( self.degree_lst_file, "degree" )
        self.tag_using_word_list ( self.degrees, Tagset.DEG )

    def __repr__ ( self ):
        ret:str = "";
        ret += f"Degrees : {len(self.degrees)}\n"
        for wp in self.word_pos:
            ret += f"{wp}\n"
        return ret;
