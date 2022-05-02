import csv
from Word_Pos_List_Structure.Word_Pos_List_Structure import Word_POS_List
from Tagset.Tagset import Tagset

class Conjunction_Finder:

    conjunction_lst_file = "src/CSV_files/conjunction_list.csv"
    conjunctions = []
    word_pos = []

    def __init__ ( self, word_pos:Word_POS_List ):
        self.word_pos = word_pos
        self.init_conjunctions ()
        self.mark_conjunctions ()

    def init_conjunctions ( self ):
        items = []
        with open ( self.conjunction_lst_file, 'r' ) as f:
            reader = csv.DictReader ( f )
            items = list ( reader )
        for item in items:
            self.conjunctions.append ( item.get ( 'conjunction' ) )

    def mark_conjunctions ( self ):
        for item in self.word_pos:
            for conjunction in self.conjunctions:
                if item.word == conjunction:
                    item.pos_list.append ( Tagset.CNJ )
                    print ( "Conjunction found" )

    def __repr__ ( self ):
        return str (
                "Word"
                f"{self.word_pos}\n"
                # f"{self.conjunctions}\n"
                )
