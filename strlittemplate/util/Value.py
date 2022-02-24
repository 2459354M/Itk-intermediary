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

