# -*- encoding: utf-8 -*-

import pandas as pd
import json
import os

from nltk import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer


def pre(tags):
    with open('./data/stopwords-es.json', 'r') as f:
        stop_js = json.load(f)
        ES_STOPWORDS = stop_js['words']

    clean = []

    tokenizer = RegexpTokenizer(r'\w+')
    for tag in tags:
        clean.extend(tokenizer.tokenize(tag.lower()))

    tokens = []
    for tag in clean:
        if tag not in ES_STOPWORDS and not tag.isnumeric():
            tokens.append(tag)

    # apply stemmer
    stemmer = SnowballStemmer('spanish')
    stemmed_tokens = []
    for token in tokens:
        stemmed_tokens.append(stemmer.stem(token))

    return stemmed_tokens


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

    article_tags = pre(read_tags(article))
    # print(article_tags)

    for source in sources:
        for category in categories:
            dir_path = './data/' + source + '/' + category + '/'
            for file in os.listdir(dir_path):
                filepath = dir_path + file
                if filepath != article:  # no hacer la compracion con el mismo
                    tags = pre(read_tags(filepath))
                    df.loc[-1] = [filepath, tags, sim(article_tags, tags)]
                    df.index = df.index + 1

    # order by DES and reset index
    df = df.sort_values('similarity', ascending=False)
    df.reset_index(inplace=True)
    del df['index']
    return df


# if __name__ == '__main__':
#     all_sim('./data/elMundo/ciencia/ciencia.2020-04-08.001.json', ['elMundo', 'elPais', '20Minutos'],
#             ['ciencia', 'salud', 'tecnologia'])
