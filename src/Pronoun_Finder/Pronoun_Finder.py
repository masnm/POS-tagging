import csv
from bisect import bisect_left
from Word_Pos_List_Structure.Word_Pos_List_Structure import Word_POS_List
from Tagset.Tagset import Tagset

class Pronoun_Finder:

    filename = "src/CSV_files/pronoun_list.csv"
    word_pos = []
    pronouns = []

    def __init__ ( self, word_pos:Word_POS_List ):
        self.word_pos = word_pos
        self.init_pronouns ()
        self.mark_pronouns ()

    def init_pronouns ( self ):
        items = []
        with open ( self.filename, 'r' ) as f:
            reader = csv.DictReader ( f )
            items = list ( reader )
        for item in items:
            self.pronouns.append ( item.get ( 'pronoun' ) )
        self.pronouns.sort ()

    def mark_pronouns ( self ):
        for item in self.word_pos:
            index = bisect_left ( self.pronouns, item.word )
            if index != len ( self.pronouns ) and self.pronouns[index] == item.word:
                item.pos_list.append ( Tagset.PP )

    def __repr__ ( self ):
        return str ( # f"Pronoun List : {self.pronouns}\n"
                f"Word with PP Tags : {self.word_pos}\n"
                )
