# -*- encoding: utf-8 -*-

import pandas as pd
import json
import os


def read_tags(filepath):
    with open(filepath, 'r') as f:
        js = json.load(f)
        f.close()
    return js['processed_tags']

def read_title(filepath):
    with open(filepath, 'r') as f:
        js = json.load(f)
        f.close()
    return js['title']


def sim(tag_doc1, tag_doc2):
    if tag_doc1 == tag_doc2:
        return 1.0
    else:
        num = 2 * len(set(tag_doc1).intersection(tag_doc2))
        den = len(tag_doc1) + len(tag_doc2)
        return num / den


def all_sim(article, sources, categories):
    df = pd.DataFrame(columns=['file', 'tags', 'similarity'])

    article_tags = read_tags(article)
    # print(article_tags)

    for source in sources:
        for category in categories:
            dir_path = './data/' + source + '/' + category + '/'
            for file in os.listdir(dir_path):
                filepath = dir_path + file
                if filepath != article:  # no hacer la compracion con el mismo
                    tags = read_tags(filepath)
                    title = read_title(filepath)
                    df.loc[-1] = [filepath, title, sim(article_tags, tags)]
                    df.index = df.index + 1

    # drop items with similarity <= 5%
    no_similarity = df[df['similarity'] <= 0.05].index
    df.drop(no_similarity, inplace=True)

    # order by DES and reset index
    df = df.sort_values('similarity', ascending=False)
    df.reset_index(inplace=True)
    del df['index']
    return df
