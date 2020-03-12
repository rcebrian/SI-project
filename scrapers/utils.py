# -*- encoding: utf-8 -*-
import json


def store_data(directory, category, content, id):
    path = "../data/" + directory + "/" + category + "/" + category + "." + id + ".json"
    with open(path, 'w') as f:
        json.dump(content, f)
