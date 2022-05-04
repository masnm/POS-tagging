from CSV_File_To_List.CSV_File_To_List import CSV_File_To_List

class Word_Seperator ( CSV_File_To_List ):

    filename = "src/CSV_files/punctuation_mark.csv"
    sentence = ""
    words = []
    punctuations = []

    def __init__ ( self, sentence:str ):
        self.sentence = sentence
        self.punctuations = self.file_to_list ( self.filename, "mark" )
        self.seperate_words ()

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
