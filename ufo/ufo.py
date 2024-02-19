def is_number(my_string):
    """
    Function which takes a string as input and returns True if it can be
    interpreted as a number, ie, converted into a float (and also therefore
    an int)
    """
    try:
        float(my_string)
        return True
    except ValueError:
        return False
