import os
import os.path
import shutil

def iteration(path):
    dirs=[list_ for list_ in os.listdir(path) if os.path.isdir(list_)]
    files=[file_ for file_ in os.listdir(path) if os.path.isfile(list_)]
    for i in files:
        if 'a' in i:
            print(hh)

    if not len(dirs):
        iteration()


