def add_to_dictionary(dict, key, val):
    """ This code adds the arguments of a key and value pair into the dictionary called dict and returns the updated dictionary.

    :param dict: dictionary
    :param key: string
    :param val: float
    :return: dictionary
    """
    if type(key) != str:
        raise TypeError("Key is not a string")
    dict[key] = val
    return dict
