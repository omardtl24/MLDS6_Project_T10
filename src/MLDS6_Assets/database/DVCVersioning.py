import json
import os

def loadData(path):
    with open(path) as f:
        return f.read()
    return None