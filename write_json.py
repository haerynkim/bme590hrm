import json

def write_json(filename, dict):
    """

    :return:
    """
    #check if filename = string
    filename = filename.replace('csv','json')
    idx = filename.rfind('/')+1
    jsonname = filename[idx:]
    with open(jsonname, 'w') as file:
        json.dump(dict, file)
    return file