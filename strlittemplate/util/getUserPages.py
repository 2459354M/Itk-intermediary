import userPages
import os
import sys
import inspect


# KetZoomer - https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir)


print("success importing userPages")
