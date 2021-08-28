from BigNamesList.big_names_list import big_names_list

name_list = big_names_list()
name_list = set([x.lower() for x in name_list])

def check_for_name(string):    
    """
    Input: string
    Returns: bool
    
    Determines if any part of the string is contained in the name_list 
    """
    contains_name = any(x in string for x in name_list)
    return contains_name