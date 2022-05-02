from Sentence_Scanner.Sentence_Scanner import *
from Word_Seperator.Word_Seperator import *
from Word_Pos_List_Structure.Word_Pos_List_Structure import *
from Pronoun_Finder.Pronoun_Finder import *
from Conjunction_Finder.Conjunction_Finder import *

class Run:

    Sentence:Sentence_Scanner
    word_seperator:Word_Seperator
    word_pos_list:Word_Pos_List_Structure
    pronoun_finder:Pronoun_Finder
    conjunction_finder:Conjunction_Finder

    def __init__ ( self ):
        pass

    def start ( self ):
        # Taking bangla sentence as input
        Sentence = Sentence_Scanner ()
        # Seperate the words into a list
        word_seperator = Word_Seperator ( Sentence.sentence )
        # Creating the struct with word and pos list
        word_pos_list = Word_Pos_List_Structure ( word_seperator.words )
        # Pronoun finder class
        pronoun_finder = Pronoun_Finder ( word_pos_list.word_pos )
        # Conjunction finder class
        conjunction_finder = Conjunction_Finder ( pronoun_finder.word_pos )
        print ( conjunction_finder )

if __name__ == "__main__":
    run = Run ()
    run.start ()
