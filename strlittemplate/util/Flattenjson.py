import json

from isort import file

def flattenjson(d):
    if type(d) != dict:
        raise ValueError('value d is not a dictionary, cannot flatten!')
        return False
    else:
        return start(d)


##taken from https://stackoverflow.com/questions/51359783/how-to-flatten-multilevel-nested-json user: Bostjan
def start(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '>')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '>')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    
    strlistpair = {}

    for i in out.keys():
        strlistpair[i] = i.split(">")

    return strlistpair

def test(filepath):
    with open(filepath) as file:
        data = json.load(file)
        data = data[0]
    print(flattenjson(data))