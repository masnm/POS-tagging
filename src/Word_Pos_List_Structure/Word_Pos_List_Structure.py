class Word_POS_List:

    word = ""
    pos_list = []

    def __init__ ( self, word:str ):
        self.word = word
        self.pos_list = []

    def __repr__ ( self ):
        return str ( f"[{self.word} {self.pos_list}]" )

class Word_Pos_List_Structure:

    word_pos = []

    def __init__ ( self, words ):
        self.create_word_pos_list ( words )

    def create_word_pos_list ( self, words ):
        for word in words:
            self.word_pos.append ( Word_POS_List ( word ) )

    def __repr__ ( self ):
        return str ( f"{ self.word_pos }" )
