import random

def colour(list):
    random.seed = 0
    colours = []
    for i in range(len(list)):
        colours.append('rgb(' +
        str(random.randint(0, 255)) + ',' + str(random.randint(0, 255)) + ',' + str(random.randint(0, 255))+ ")")

    return colours