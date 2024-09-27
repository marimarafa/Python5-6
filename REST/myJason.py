import json
import jsonschema
import requests
import sys


def JsonSerialize(data, sFile):
    with open(sFile, "w") as write_file:
        json.dump(data, write_file,indent=4)

def JsonDeserialize(sFile):
    with open(sFile, "r") as read_file:
        return json.load(read_file)