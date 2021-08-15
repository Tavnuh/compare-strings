# Imports

import pandas as pd
import numpy as np
import Levenshtein



from helpers.helpers import calculate_cosine_similarity
from helpers.helpers import check_for_name
from helpers.helpers import remove_punc_nums
from helpers.helpers import split_email



#-----------------------------------------------------------------------------

def compare_strings(input_1, 
                    input_2, 
                    email = None, 
                    method = 'lev_props',
                    precision = 2,
                    check_names = False):
   
    """
    CORE FUNCTION:
    First, this function tests if the values passed to 'input_1' and 'input_2' 
    are of type string, or if they are Pandas Series'. If inputs are strings, 
    the first 'if' block executes. If Pandas Series', second 'elif' block 
    executes. If neither, 'else' block executes and error is raised asking user 
    for strings or Series'

    1. If input = string:

      i.   String cleaning function remove_punc_nums() executes with additional 
           split_email() on first input if email == 1 or on second input if 
           email == 2
           
      ii.  If method == lev_props, the Levenshtein Distance between the two 
           inputs is returned as a proportion of the first input.
           
           Outputs a float between 0 and 1, where:    
               0 = exact similarity
               1 = maximum dissimilarity
               
           If method == lev_abs, the absolute Levenshtein Distance is returned
           
           Outputs an int representing the minimum number of 
           single-character edits (i.e. insertions, deletions or substitutions) 
           required to change one string into the other. 
               
           If method == cosine, (1- cosine similarity) is returned.
           Outputs a float between 0 and 1, where:    
               0 = exact similarity
               1 = maximum dissimilarity
 

    2. If input = Series
        
       i.    All functions are vectorized using np.vectorize
       
       ii.   If method == lev_props, the Levenshtein Distance between the two 
             inputs is returned as a proportion of the first input.
            
             Outputs a float between 0 and 1, where:    
                 0 = exact similarity
                 1 = maximum dissimilarity             
             
             If method == lev_abs, the absolute Levenshtein calculated is 
             returned for matching pairs in both input series'
             
           Outputs an int representing the minimum number of 
           single-character edits (i.e. insertions, deletions or substitutions) 
           required to change one string into the other.
             
       v.  The two original series' and selected method's output are returned 
           as 3 columns in a new Dataframe
    
    
    ***Error Handling***
        i.   Input data types: This function expects inputs 1 and 2 to be 
             either strings or Pandas series. Any other dtype passed to the 
             function will raise an error.
             
             Lists may be accepted in future
        
        
        ii.  ZeroDivision errors: If any of the values passed to input 1 are
        empty strings and the lev_props method is selected, the function will
        return np.inf. This is because the lev_props method tries to divide
        the calculated levenshtein distance by the length of the first string. 
        

    """   
    

    
    #tests if the inputs are strings
    if isinstance(input_1, str) and isinstance(input_2, str):
    
        # Lower casing both strings
        lower_string_1 = str.lower(input_1)
        lower_string_2 = str.lower(input_2)
        
        
        # If the first string is an email address, split it on the '@' then 
        # strip punctuation and numbers from both
        if email == 1:
            user_name = split_email(lower_string_1)
            
            stripped_string_1 = remove_punc_nums(user_name)
            stripped_string_2 = remove_punc_nums(lower_string_2)
            
            
        # If the second string is an email address, split it on the '@' then 
        # strip punctuation and numbers from both
        elif email == 2:
            stripped_string_1 = remove_punc_nums(lower_string_1)
            
            user_name = split_email(lower_string_2)
            stripped_string_2 = remove_punc_nums(user_name)
            
            
        # If neither string was an email address, only strip punctuation and 
        # numbers from both
        elif email == None:
            stripped_string_1 = remove_punc_nums(lower_string_1)
            stripped_string_2 = remove_punc_nums(lower_string_2)
            
        
            
        # Selects the method of distance calculation
        
        # Levenshtein Proportions - levenshtein distance as a proportion of 
        # the length of the first string 
        # If the true proportion is > 1, return 1 (maximum)
        if method == 'lev_props':
            try: 
                distance = round(Levenshtein.distance(stripped_string_1,
                                                      stripped_string_2) / 
                                 len(stripped_string_1),precision)
                if distance > 1:
                    return 1
                else:
                    return distance
            
            except ZeroDivisionError:
                
                return np.inf
        
        
        # Levenshtein Distance - The absolute levenshtein distance between the 
        # two strings    
        elif method == 'lev_abs':
            distance = Levenshtein.distance(stripped_string_2,
                                            stripped_string_1)
            
            return distance
        
        # Cosine Dissimilarity - the inverse of the Cosine Similarity between 
        # the two strings
        elif method == 'cosine':
            print("Cosine similarity calculation for strings coming soon!")
            
            #cos_similarity = calculate_cosine_similarity([stripped_string_2,
            #                                              stripped_string_1])
            
            #return round( 1- cos_similarity,2)
        
        
    # Tests if the inputs are Pandas Series
    elif isinstance(input_1, pd.Series) and isinstance(input_2, pd.Series):
        
        #lowers each value in both series'
        series_1 = input_1.str.lower()
        series_2 = input_2.str.lower()

        
        # If the first series contains email addresses, split values on the '@' 
        # then strip punctuation and numbers from both
        if email == 1:
            usernames = np.vectorize(split_email)(series_1)
            array_1_clean = np.vectorize(remove_punc_nums)(usernames)
            array_2_clean = np.vectorize(remove_punc_nums)(series_2)
        
        # If the second series contains email addresses, split values on the '@' 
        # then strip punctuation and numbers from both
        elif email == 2:
            array_1_clean = np.vectorize(remove_punc_nums)(series_1)
            usernames = np.vectorize(split_email)(series_2)
            array_2_clean = np.vectorize(remove_punc_nums)(usernames)
        
        
        # If neither series contains email addresses, only strip punctuation
        # and numbers
        elif email == None:
            array_1_clean = np.vectorize(remove_punc_nums)(series_1)
            array_2_clean = np.vectorize(remove_punc_nums)(series_2)

        
        
        # Levenshtein Proportions - levenshtein distance as a proportion of 
        # the length of the first string 
        if method == 'lev_props':
            
            # calculates the lev distance between the elements of the arrays
            distances = np.vectorize(Levenshtein.distance)(array_1_clean, 
                                                           array_2_clean)
            
            # calculates the length of each element in array_1_clean
            array_1_lengths = np.vectorize(len)(array_1_clean)
            
            # calculates levenshtein proportions 
            levenshtein_proportions = distances / array_1_lengths
            
            # converts the proportions array to series
            levenshtein_proportions = pd.Series(levenshtein_proportions)
            
            # create a DF that contains the inputs along with lev_pros
            df = pd.DataFrame()
            df[input_1.name] = input_1
            df[input_2.name] = input_2
            df['levenshtein_proportions'] = levenshtein_proportions
            
            
            
            """"
            check_names intended to be used in the case where one of the inputs
            contains email addresses. For example, if the user only cares 
            about the similarity of a name field and an email field IF that 
            email contains a name, check_names would be True. 
            
            If True passed to check_names, assign a new column to DF with 
            boolean returned from check_for_name function
            
            This isn't foolproof, as the list of names contains some smaller
            strings which may be found in words that are not names.
            
            """
            
            
            if check_names == True:
                if email == 1:
                    contains_name = np.vectorize(check_for_name)(array_1_clean)
                    df[f'{input_1.name}_contains_name'] = contains_name
                    
                elif email == 2:
                    contains_name = np.vectorize(check_for_name)(array_2_clean)
                    df[f'{input_2.name}_contains_name'] = contains_name
                    

        
        
        # Levenshtein Distance - The absolute levenshtein distance between the 
        # elements of the two arrays
        elif method == 'lev_abs':
            
            #calculates the levenshtein distance between the elements of arrays
            distances = np.vectorize(Levenshtein.distance)(array_1_clean, 
                                                           array_2_clean)
            
            # converts the distances array to series
            distances = pd.Series(distances)

            # create a DF that returns the inputs along with the lev_distances
            df = pd.DataFrame()
            df[input_1.name] = input_1
            df[input_2.name] = input_2
            df['levenshtein_distances'] = distances
            
            return df
        
        
        elif method == 'cosine':
            print("Cosine similarity calculation for Series' coming soon!")
            
    else:
        dtype_exception_msg = """{} Not accepted yet""".format(type(input_1))
        raise Exception(dtype_exception_msg)
    
    