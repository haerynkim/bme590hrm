import json


def write_json(filename, dict):
    """
    This function takes a string and retrieves the filename to which it will generate a new json file and populate with
    a given dictionary.

    :param filename: str
    :param dict: dictionary
    """
    filename = filename.replace('csv', 'json')
    idx = filename.rfind('/') + 1
    jsonname = filename[idx:]
    with open(jsonname, 'w') as file:
        json.dump(dict, file)
