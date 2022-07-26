from Word_Pos_List_Structure.Word_Pos_List_Structure import Word_POS_List
from Tag_Using_Word_List.Tag_Using_Word_List import Tag_Using_Word_List
from Tag_Using_Suffix_List.Tag_Using_Suffix_List import Tag_Using_Suffix_List
from Tag_Using_Prefix_Suffix_List.Tag_Using_Prefix_Suffix_List import Tag_Using_Prefix_Suffix_List
from CSV_File_To_List.CSV_File_To_List import CSV_File_To_List
from CSV_File_To_List_Of_List.CSV_File_To_List_Of_List import CSV_File_To_List_Of_List
from Tagset.Tagset import Tagset

class Verb_Finder ( CSV_File_To_List, CSV_File_To_List_Of_List, Tag_Using_Word_List, Tag_Using_Suffix_List, Tag_Using_Prefix_Suffix_List ):

    verb_lst_file = "src/CSV_files/verb_list.csv"
    verb_suffixe_lst_file = "src/CSV_files/verb_suffixe_list.csv"
    non_finite_prefix_suffix_lst_file = "src/CSV_files/non_finite_verb_suffix_prefix_list.csv"
    verbs = []
    verb_suffixes = []
    word_pos = []
    nf_verb_ps = []

    def __init__ ( self, word_pos:Word_POS_List ):
        self.word_pos = word_pos
        self.verbs = self.file_to_list ( self.verb_lst_file, "verb" )
        self.tag_using_word_list ( self.verbs, Tagset.VF )
        self.verb_suffixes = self.file_to_list ( self.verb_suffixe_lst_file, "verb_suffix" )
        self.tag_using_suffix_list ( self.verb_suffixes, Tagset.VF )
        self.nf_verb_ps = self.file_to_list_of_list ( self.non_finite_prefix_suffix_lst_file, "nfv_prefix", "nfv_suffix" )
        self.tag_using_prefix_suffix_list ( self.nf_verb_ps, Tagset.VNF )

    def __repr__ ( self ):
        ret:str = "";
        for wp in self.word_pos:
            ret += f"{wp}\n"
        return ret;
