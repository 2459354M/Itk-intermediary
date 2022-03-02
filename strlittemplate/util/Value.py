def getValue(data,strlist,string):
    mylist = strlist[string]
    for i in mylist:
        try: ## case if value is part of list
            i = int(i)
        except:
            pass

        try:
            data = data[i]
        except:
            ## key selected by user may only have values in some instances
            return None
    return data


def count(l):
    d = {}
    for i in l:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
            
    return d

def getPairings(value1,value2):
    mylist = value1.copy()
    mylist.extend(value2)
    mylist = list(set(mylist))
    source = []
    for i in value1:
        source.append(mylist.index(i))

    target = []
    for i in value2:
        target.append(mylist.index(i))

    a = zip(source, target)

    d = count(a)
    source, target, value = [], [], []
    for i in d.keys():
        source.append(i[0])
        target.append(i[1])
        value.append(d[i])

    return mylist,source,target,value
