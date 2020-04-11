import json
import os


def read_json(filepath):
    with open(filepath, 'r') as f:
        js = json.load(f)
        f.close()
    return js


def count_files(source, category):
    return len(os.listdir('./data/' + source + '/' + category))
