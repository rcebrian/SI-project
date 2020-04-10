import os

def count_files(source, category):
    return len(os.listdir('./data/' + source + '/' + category))
