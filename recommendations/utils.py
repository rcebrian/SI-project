# -*- encoding: utf-8 -*-

import pandas as pd
import json
import os


def read_tags(filepath):
    with open(filepath, 'r') as f:
        js = json.load(f)
        f.close()
    return js['processed_tags']


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
                    df.loc[-1] = [filepath, tags, sim(article_tags, tags)]
                    df.index = df.index + 1

    # order by DES and reset index
    df = df.sort_values('similarity', ascending=False)
    df.reset_index(inplace=True)
    del df['index']
    return df
