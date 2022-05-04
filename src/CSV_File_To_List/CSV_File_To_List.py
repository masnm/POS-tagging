import csv

class CSV_File_To_List:

    def __init__ ( self ):
        pass

    def file_to_list ( self, filename:str, tag:str ) -> []:
        items = []
        ret_list = []
        with open ( filename, 'r' ) as f:
            reader = csv.DictReader ( f )
            items = list ( reader )
        for item in items:
            ret_list.append ( item.get ( tag ) )
        ret_list.sort ()
        return ret_list
