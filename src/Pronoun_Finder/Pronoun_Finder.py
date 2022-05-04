from CSV_File_To_List.CSV_File_To_List import CSV_File_To_List
from Word_Pos_List_Structure.Word_Pos_List_Structure import Word_POS_List
from Tagset.Tagset import Tagset

class Pronoun_Finder ( CSV_File_To_List ):

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
        self.pronouns = self.file_to_list ( self.filename, "pronoun" )
        self.prefixes = self.file_to_list ( self.prefix_file, "prefix" )
        self.possessive_pronouns = self.file_to_list ( self.singular_pp_file, "singular" )
        self.possessive_pronouns += ( self.file_to_list ( self.plural_pp_file, "plural" ) )
        self.mark_pronouns ()

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
