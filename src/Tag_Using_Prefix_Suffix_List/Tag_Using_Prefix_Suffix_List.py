import warnings
from Tagset.Tagset import Tagset
from Word_Pos_List_Structure.Word_Pos_List_Structure import Word_POS_List

class Tag_Using_Prefix_Suffix_List:

    def __init__ ( self ):
        pass

    def tag_using_prefix_suffix_list ( self, word_of_words, tag:Tagset ):
        for item in self.word_pos:
            for words in word_of_words:
                warnings.warn ( 'little bit of hack hrere with this 1 in next line' )
                if item.word.startswith(words[0], 1) and item.word.endswith(words[-1]):
                    item.pos_list.append ( tag )
            # Removing repetation form the list
            item.pos_list = [*{*item.pos_list}]
