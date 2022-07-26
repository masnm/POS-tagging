from Tagset.Tagset import Tagset
from Word_Pos_List_Structure.Word_Pos_List_Structure import Word_POS_List

class Tag_Using_Suffix_List:

    def __init__ ( self ):
        pass

    def tag_using_suffix_list ( self, words:str, tag:Tagset ):
        for item in self.word_pos:
            for word in words:
                if item.word.endswith(word):
                    item.pos_list.append ( tag )
            # Removing repetation form the list
            item.pos_list = [*{*item.pos_list}]
