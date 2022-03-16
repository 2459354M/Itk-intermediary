import pandas as pd
import datetime

# goes through a list to recursively obtain the value in a dictionary


def getValue(data, strlist, string):
    mylist = strlist[string]
    for i in mylist:
        try:  # case if value is part of list
            i = int(i)
        except BaseException:
            pass

        try:
            data = data[i]
        except BaseException:
            # key selected by user may only have values in some instances
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

# returns a dictionary which maps 2 values to how many times those values
# occur in a single instance


def getPairings(value1, value2):
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

    return mylist, source, target, value

# counts occurances and returns DataFrame


def GetCountDF(value1, index1):
    value1 = count(value1)
    x, y = [], []

    for key, value in value1.items():
        x.append(key)
        y.append(value)
    x_name = str(index1)
    value1 = pd.DataFrame({
        x_name: x,
        'count': y
    })

    return value1, x_name


def parse_date(datestr):
    try:
        date = datestr[0:10].split("-")
        time = datestr[11:19].split(":")
        ms = int(datestr[-4:-1]) * 1000
        print(time)
        date = [int(i) for i in date]
        print(date)
        time = [int(j) for j in time]
        print(time)
        return datetime.datetime(*date, *time, ms)
    except BaseException:
        print("could not parse date")
