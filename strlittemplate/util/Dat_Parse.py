import pandas as pd
import numpy as np

# generic parsing method for getting tables in a data file


def parse(myfile):
    data = myfile.read().decode("utf-8")
    mylist = []
    y = 0
    z = 0
    # splits by line
    for h, i in enumerate(data.split("\n")):
        # splits by tab
        for j in i.split("\t"):
            try:
                mylist.append(float(j))
                # if we find a matching case we store how many columns and where the line is we
                # found it
                if y == 0:
                    y = h - 1
                    z = len(i.split("\t"))
            except BaseException:
                break
    # change to 2d aray
    arr = np.array(mylist).reshape(int(len(mylist) / z), z)

    # assumes line before is header
    names = ((data.split("\n")[y]).strip().replace(
        "[", "(").replace("]", ")")).split(" ")

    df = pd.DataFrame(arr, columns=names)
    return df, names
