def getValue(data,strlist,string):
    mylist = strlist[string]
    for i in mylist:
        try:
            i = int(i)
        except:
            pass
        data = data[i]
    return data


def count(l):
    d = {}
    print(l)
    for i in l:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    return d

