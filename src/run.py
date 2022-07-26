from Sentence_Scanner.Sentence_Scanner import Sentence_Scanner
from Word_Seperator.Word_Seperator import Word_Seperator
from Word_Pos_List_Structure.Word_Pos_List_Structure import Word_Pos_List_Structure
from Pronoun_Finder.Pronoun_Finder import Pronoun_Finder
from Conjunction_Finder.Conjunction_Finder import Conjunction_Finder
from Conditional_Finder.Conditional_Finder import Conditional_Finder
from Interjection_Finder.Interjection_Finder import Interjection_Finder
from Interrogative_Finder.Interrogative_Finder import Interrogative_Finder
from Negative_Finder.Negative_Finder import Negative_Finder
from Verb_Finder.Verb_Finder import Verb_Finder
from Onusorgu_Finder.Onusorgu_Finder import Onusorgu_Finder
from Degree_Finder.Degree_Finder import Degree_Finder
from Adjective_Of_Adjective_Finder.Adjective_Of_Adjective_Finder import Adjective_Of_Adjective_Finder
from Adjective_Finder.Adjective_Finder import Adjective_Finder

class Run:

    Sentence:Sentence_Scanner
    word_seperator:Word_Seperator
    word_pos_list:Word_Pos_List_Structure
    pronoun_finder:Pronoun_Finder
    conjunction_finder:Conjunction_Finder
    conditional_finder:Conditional_Finder
    interjection_finder:Interjection_Finder
    verb_finder:Verb_Finder
    onusorgu_finder:Onusorgu_Finder
    degree_finder:Degree_Finder
    adjective_of_adjective_finder:Adjective_Of_Adjective_Finder
    adjective_finder:Adjective_Finder

    def __init__ ( self ):
        pass

    def start ( self, line:str ):
        # Taking bangla sentence as input
        Sentence = Sentence_Scanner ( line )
        # Seperate the words into a list
        word_seperator = Word_Seperator ( Sentence.sentence )
        # Creating the struct with word and pos list
        word_pos_list = Word_Pos_List_Structure ( word_seperator.words )
        # Pronoun finder class
        pronoun_finder = Pronoun_Finder ( word_pos_list.word_pos )
        # Conjunction finder class
        conjunction_finder = Conjunction_Finder ( pronoun_finder.word_pos )
        # Conditional finder class
        conditional_finder = Conditional_Finder ( conjunction_finder.word_pos )
        # Interjection finder class
        interjection_finder = Interjection_Finder ( conditional_finder.word_pos )
        # Interrogative finder class
        interrogative_finder = Interrogative_Finder ( interjection_finder.word_pos )
        # Negative finder class
        negative_finder = Negative_Finder ( interrogative_finder.word_pos )
        # Verb finder class
        ## TODO: Verb finder in not implemented yet
        verb_finder = Verb_Finder ( negative_finder.word_pos )
        # Onusorgu finder class
        onusorgu_finder = Onusorgu_Finder ( verb_finder.word_pos )
        # Degree finder class
        degree_finder = Degree_Finder ( onusorgu_finder.word_pos )
        # Adjective of Adjective finder class
        adjective_of_adjective_finder = Adjective_Of_Adjective_Finder ( degree_finder.word_pos )
        # Ajdective finder class
        adjective_finder = Adjective_Finder ( adjective_of_adjective_finder.word_pos )
        print ( adjective_finder )

if __name__ == "__main__":
    run = Run ()
    with open ( 'test_inputs/run_input' ) as openfileobj:
        for line in openfileobj:
            run.start ( line );
