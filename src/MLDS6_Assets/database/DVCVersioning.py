import json
import os

def loadData(path):
    '''
    Load a file content and return it

    Param:
        path (str) : Folder where the 
    '''
    with open(path) as f:
        return f.read()
    return None