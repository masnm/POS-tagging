from Sentence_Scanner.Sentence_Scanner import *
from Word_Seperator.Word_Seperator import *
from Word_Pos_List_Structure.Word_Pos_List_Structure import *
from Pronoun_Finder.Pronoun_Finder import *
from Tagset.Tagset import *

# Taking bangla sentence as input
Sentence = Sentence_Scanner ()
# print ( "Sentence Scanner Object" )
# print ( Sentence )

# Seperate the words into a list
word_seperator = Word_Seperator ( Sentence.sentence )
# print ( "Word Seperator Object" )
# print ( word_seperator )
 
# Creating the struct with word and pos list
word_pos_list = Word_Pos_List_Structure ( word_seperator.words )
# print ( word_pos_list )

# Pronoun finder class
pronoun_finder = Pronoun_Finder ( word_pos_list.word_pos )
print ( pronoun_finder )
