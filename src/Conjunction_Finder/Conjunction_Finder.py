from CSV_File_To_List.CSV_File_To_List import CSV_File_To_List
from Tag_Using_Word_List.Tag_Using_Word_List import Tag_Using_Word_List
from Word_Pos_List_Structure.Word_Pos_List_Structure import Word_POS_List
from Tagset.Tagset import Tagset

class Conjunction_Finder ( CSV_File_To_List, Tag_Using_Word_List ):

    conjunction_lst_file = "src/CSV_files/conjunction_list.csv"
    conjunctions = []
    word_pos = []

    def __init__ ( self, word_pos:Word_POS_List ):
        self.word_pos = word_pos
        self.conjunctions = self.file_to_list ( self.conjunction_lst_file, "conjunction" )
        self.tag_using_word_list ( self.conjunctions, Tagset.CNJ )

    def __repr__ ( self ):
        return str (
                "Word"
                f"{self.word_pos}\n"
                # f"{self.conjunctions}\n"
                )
