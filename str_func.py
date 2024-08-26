def get_upper(s: str):
    """get UPPER string"""
    return s.upper()


def get_capitalise(s: str):
    """ get all words in string capitalized"""
    l = [i.capitalize() for i in s.split()]
    return ' '.join(l)
