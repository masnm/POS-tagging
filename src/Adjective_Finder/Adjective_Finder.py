from Word_Pos_List_Structure.Word_Pos_List_Structure import Word_POS_List
from Tag_Using_Word_List.Tag_Using_Word_List import Tag_Using_Word_List
from Tag_Using_Suffix_List.Tag_Using_Suffix_List import Tag_Using_Suffix_List
from CSV_File_To_List.CSV_File_To_List import CSV_File_To_List
from Tagset.Tagset import Tagset

class Adjective_Finder ( CSV_File_To_List, Tag_Using_Word_List, Tag_Using_Suffix_List ):

    adjective_suffix_lst_file = "src/CSV_files/adjectiv_suffix_list.csv"
    adjective_suffixes = []
    word_pos = []
    suffix_ender = ['ই','ও']

    def __init__ ( self, word_pos:Word_POS_List ):
        self.word_pos = word_pos
        self.adjective_suffixes = self.file_to_list ( self.adjective_suffix_lst_file, "adjective suffix" )
        self.tag_using_suffix_list ( self.adjective_suffixes, Tagset.AD )
        for adj_suf in self.adjective_suffixes:
            for suf_end in self.suffix_ender:
                adj_suf += suf_end
        self.tag_using_suffix_list ( self.adjective_suffixes, Tagset.AD )

    def __repr__ ( self ):
        ret:str = "";
        ret += f"Adjective : {len(self.adjective_suffixes)}\n"
        for wp in self.word_pos:
            ret += f"{wp}\n"
        return ret;
