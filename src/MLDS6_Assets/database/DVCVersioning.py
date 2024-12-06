import json
import os

def loadCredentials(path):
    with open(path) as f:
        os.environ["GDRIVE_CREDENTIALS_DATA"] = f.read()