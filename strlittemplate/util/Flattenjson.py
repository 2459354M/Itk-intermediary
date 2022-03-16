import json
# takes a json style dictionary and converts it to a dictionary containing
# a string and list pairing


def flattenjson(d):
    if isinstance(d, dict):
        return start(d)
    elif isinstance(d, list):
        flatdatakeys = start(d[0])
        for i in d:
            attempt = flattenjson(i)
            flatdatakeys = {x: flatdatakeys[x]
                            for x in flatdatakeys if x in attempt}
        return flatdatakeys
    else:
        raise ValueError("d is not a list or dictionary")
        return false


# taken from
# https://stackoverflow.com/questions/51359783/how-to-flatten-multilevel-nested-json
# user: Bostjan
def start(y):
    out = {}

    def flatten(x, name=''):
        if isinstance(x, dict):
            for a in x:
                flatten(x[a], name + a + '>')
        elif isinstance(x, list):
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
