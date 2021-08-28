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
