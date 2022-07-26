import csv

class CSV_File_To_List_Of_List:

    def __init__ ( self ):
        pass

    def file_to_list_of_list ( self, filename:str, taga:str, tagb:str ):
        items = []
        ret_list = []
        with open ( filename, 'r' ) as f:
            reader = csv.DictReader ( f )
            items = list ( reader )
        for item in items:
            sublist = []
            sublist.append ( item.get ( taga ) )
            sublist.append ( item.get ( tagb ) )
            ret_list.append ( sublist )
        ret_list.sort ()
        return ret_list
