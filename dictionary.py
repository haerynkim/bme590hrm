def add_to_dictionary(dict, key, val):
    #test if key is string
    if type(key) != str:
        raise TypeError("Key is not a string")
    dict[key] = val
    return dict