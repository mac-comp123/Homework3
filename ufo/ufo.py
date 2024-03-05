def is_number(my_string: str) -> bool:
    """
    Check if a string can be interpreted as a number

    @my_string: a string
    @return: Ture if the string can be interpreted as a number, False otherwise
    """
    try:
        float(my_string)
        return True
    except ValueError:
        return False
