from Word_Pos_List_Structure.Word_Pos_List_Structure import Word_POS_List
from Tag_Using_Word_List.Tag_Using_Word_List import Tag_Using_Word_List
from CSV_File_To_List.CSV_File_To_List import CSV_File_To_List
from Tagset.Tagset import Tagset

class Verb_Finder ( CSV_File_To_List, Tag_Using_Word_List ):

    verb_lst_file = "src/CSV_files/verb_list.csv"
    verbs = []
    word_pos = []

    def __init__ ( self, word_pos:Word_POS_List ):
        self.word_pos = word_pos
        self.verbs = self.file_to_list ( self.verb_lst_file, "verb" )
        self.tag_using_word_list ( self.verbs, Tagset.VF )

    def __repr__ ( self ):
        return str (
                f"SZ {len(self.verbs)}\n"
                # f"Verb {self.verbs}\n"
                f"{self.word_pos}\n"
                )
