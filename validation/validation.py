import re

def validate_username(username):
    ''' validate username 
    --only alphabets and  numbers are allowed
    ---length 3 to 50 characters
    '''
    if not username:
        raise Exception("Username cannot be empty!!")
    #REGEX Pattern
    pattern = r"^[a-zA-Z0-9]{3,50}$"
    if not re.match(pattern, username):
        raise Exception("Invalid username!! Only letters and numbers are allowed minimum of 3 charcters!!")
    return True

def validate_password(password):
    ''' validate username 
    --only alphabets, numbers and special characters are allowed
    ---length 3 to 50 characters
    '''
    if not password:
        raise Exception("Password cannot be empty!!")
    #REGEX Pattern
    pattern = r"^[a-zA-Z0-9@#$&-_.]{3,50}$"
    if len(password)<3:
        raise Exception("Password must be minimum 3 characters!!")
    if not re.match(pattern, password):
        raise Exception("Invalid password!! Only letters, numbers and special characters like $#@& are allowed")
    return True