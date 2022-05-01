import csv

class Word_Seperator:

    filename = "src/CSV_files/punctuation_mark.csv"
    sentence = ""
    words = []
    punctuations = []

    def __init__ ( self, sentence:str ):
        self.init_punctuations ()
        self.sentence = sentence
        self.seperate_words ()

    def init_punctuations ( self ):
        items = []
        with open ( self.filename, 'r' ) as f:
            reader = csv.DictReader ( f )
            items = list ( reader )
        for item in items:
            self.punctuations.append ( item.get ( 'mark' ) );

    def seperate_words ( self ):
        word = ""
        for character in self.sentence:
            is_puncuation=False
            for punctuation in self.punctuations:
                if punctuation == character:
                    is_puncuation=True
                    break
            if is_puncuation:
                if word:
                    self.words.append ( word )
                word = ""
                is_puncuation=False
            else:
                word += character
        if word:
            self.words.append ( word )

    def __repr__ ( self ):
        return str ( f"sentence: {self.sentence}\n"
                f"Words: {self.words}\n"
                f"Punctuations: {self.punctuations}"
                )
