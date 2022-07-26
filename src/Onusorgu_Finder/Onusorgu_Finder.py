from Word_Pos_List_Structure.Word_Pos_List_Structure import Word_POS_List
from Tag_Using_Word_List.Tag_Using_Word_List import Tag_Using_Word_List
from CSV_File_To_List.CSV_File_To_List import CSV_File_To_List
from Tagset.Tagset import Tagset

class Onusorgu_Finder ( CSV_File_To_List, Tag_Using_Word_List ):

    onusorgu_lst_file = "src/CSV_files/onusorgu_list.csv"
    onusorgus = []
    word_pos = []

    def __init__ ( self, word_pos:Word_POS_List ):
        self.word_pos = word_pos
        self.onusorgus = self.file_to_list ( self.onusorgu_lst_file, "onusorgu" )
        self.tag_using_word_list ( self.onusorgus, Tagset.POP )

    def __repr__ ( self ):
        ret:str = "";
        for wp in self.word_pos:
            ret += f"{wp}\n"
        return ret;
