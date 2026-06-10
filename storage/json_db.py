import json
import os

DATA_DIR = "data"

def _path(file):
    return os.path.join(DATA_DIR, file)

def load(file):
    try:
        with open(_path(file), "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save(file, data):
    with open(_path(file), "w") as f:
        json.dump(data, f, indent=4)