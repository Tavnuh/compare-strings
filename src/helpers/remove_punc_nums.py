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