import csv
from bisect import bisect_left
from Word_Pos_List_Structure.Word_Pos_List_Structure import Word_POS_List
from Tagset.Tagset import Tagset

class Pronoun_Finder:

    filename = "src/CSV_files/pronoun_list.csv"
    prefix_file = "src/CSV_files/pronoun_prefix_list.csv"
    singular_pp_file = "src/CSV_files/singular_possessive_pronoun_list.csv"
    plural_pp_file = "src/CSV_files/plural_possessive_pronoun_list.csv"
    word_pos = []
    pronouns = []
    prefixes = []
    possessive_pronouns = []

    def __init__ ( self, word_pos:Word_POS_List ):
        self.word_pos = word_pos
        self.init_pronouns ()
        self.init_pronoun_prefixes ()
        self.init_possessive_pronouns ()
        self.mark_pronouns ()

    def init_pronouns ( self ):
        items = []
        with open ( self.filename, 'r' ) as f:
            reader = csv.DictReader ( f )
            items = list ( reader )
        for item in items:
            self.pronouns.append ( item.get ( 'pronoun' ) )
        self.pronouns.sort ()

    def init_pronoun_prefixes ( self ):
        items = []
        with open ( self.prefix_file, 'r' ) as f:
            reader = csv.DictReader ( f )
            items = list ( reader )
        for item in items:
            self.prefixes.append ( item.get ( 'prefix' ) )
        self.prefixes.sort ()

    def init_possessive_pronouns ( self ):
        items = []
        with open ( self.singular_pp_file, 'r' ) as f:
            reader = csv.DictReader ( f )
            items = list ( reader )
        for item in items:
            self.possessive_pronouns.append ( item.get ( 'singular' ) )
        with open ( self.plural_pp_file, 'r' ) as f:
            reader = csv.DictReader ( f )
            items = list ( reader )
        for item in items:
            self.possessive_pronouns.append ( item.get ( 'plural' ) )

    def mark_pronouns ( self ):
        for item in self.word_pos:
            # Checking for a pronoun
            for pronoun in self.pronouns:
                if pronoun == item.word:
                    item.pos_list.append ( Tagset.PP )
                for prefix in self.prefixes:
                    if pronoun + prefix == item.word:
                        item.pos_list.append ( Tagset.PP )
            # Removing repetation form the list
            item.pos_list = [*{*item.pos_list}]
            # Checking for a possessive pronoun
            for possessive_pronoun in self.possessive_pronouns:
                if possessive_pronoun[0] == '*':
                    without_star = possessive_pronoun.lstrip ( '*' )
                    if without_star in item.word:
                        item.pos_list.append ( Tagset.PPP )
                elif possessive_pronoun == item.word:
                    item.pos_list.append ( Tagset.PPP )
            # Removing repetation form the list
            item.pos_list = [*{*item.pos_list}]

    def __repr__ ( self ):
        return str (
                # f"Pronoun List : {self.pronouns}\n"
                f"Word with PP Tags : {self.word_pos}\n"
                # f"PP : {self.possessive_pronouns}\n"
                # f"Prefixes : {self.prefixes}\n"
                )
