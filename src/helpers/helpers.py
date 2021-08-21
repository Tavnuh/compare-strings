# Imports
import numpy as np
import re
from BigNamesList.big_names_list import big_names_list
### NOT YET IMPLEMENTED ###
#from sklearn.metrics.pairwise import cosine_similarity
#from sklearn.feature_extraction.text import CountVectorizer




name_list = big_names_list()
name_list = set([x.lower() for x in name_list])


#-----------------------------------------------------------------------------

# Helper functions

def split_email(email):
    """
    Input: string
    Returns: "username"
    
    If the "email = x" argument is provided to the main function, split_email
    is called. Splits string containing an email address on the '@', 
    returns 0th element.
    
    """
    
    username = str.split(email,'@')[0]

    return username




def remove_punc_nums(string):
    """
    Input: string
    Returns: "single_spaced_str"
    
    Replaces any punctuation or numbers in the give string with a space.
    Replaces all double spaces with a single space. 
    """ 
    
    no_punc_str = re.sub('[!@#$%^&*()-=+.,_]', ' ', string)
    no_num_str = re.sub(r'[0-9]+', '', no_punc_str)
    single_spaced_str = no_num_str.strip().replace('  ',' ').replace('  ', ' ')
    
    return single_spaced_str

### STILL IN DEVELOPMENT ###

#def calculate_cosine_similarity(inputs):
    
    """
    Input: list
    Returns: "csine_sim"
    
    If 'cosine' is given to the method argument in the main function,
    calculate_cosine_similarity uses sklearn's cosine_similarity which returns
    a 2x2 array. 
    
    calculate_cosine_similarity returns one element representing the cosine
    similarity between the two inputs

    """
    
    
#    vectorizer = CountVectorizer().fit_transform(inputs)
#    vectors = vectorizer.toarray()
#    csine_sim = cosine_similarity(vectors)

#    return csine_sim[1][0]


def check_for_name(string):    
    """
    Input: string
    Returns: bool
    
    Determines if any part of the string is contained in the name_list 
    """
    contains_name = any(x in string for x in name_list)
    return contains_name

def levenshtein_own():
    pass
