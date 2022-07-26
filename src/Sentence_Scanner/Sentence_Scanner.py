class Sentence_Scanner:

    sentence = ""

    def __init__( self, line:str ):
        # Creating instance attributes
        self.sentence = str ( "" )

        # Taking the sentence as input
        self.sentence = line;

    def __repr__ ( self ):
        return self.sentence
