class Sentence_Scanner:

    sentence = ""

    def __init__( self ):
        # Creating instance attributes
        self.sentence = str ( "" )

        # Taking the sentence as input
        self.get_input ()

    def get_input ( self ):
        self.sentence = input ()

    def __repr__ ( self ):
        return self.sentence
