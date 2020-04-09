import json
import math
import os

import pandas as pd
from nltk import RegexpTokenizer, FreqDist
from nltk.stem.snowball import SnowballStemmer

with open('../data/stopwords-es.json', 'r') as f:
    stop_js = json.load(f)
    ES_STOPWORDS = stop_js['words']


def pre_processing(data):
    # tokenize and remove punctuation marks
    tokenizer = RegexpTokenizer(r'\w+')
    text = tokenizer.tokenize(data.lower())

    # apply stop words list
    tokens = []
    for token in text:
        if token not in ES_STOPWORDS and not token.isnumeric():
            tokens.append(token)

    # apply stemmer
    stemmer = SnowballStemmer('spanish')
    stemmed_tokens = []
    for token in tokens:
        stemmed_tokens.append(stemmer.stem(token))

    return stemmed_tokens


def pre_process_file(path):
    with open(path, 'r') as f:
        js = json.load(f)
        f.close()

    if js['processed'] is None:
        js['processed'] = pre_processing(js['content'])
        with open(path, 'w') as f:
            json.dump(js, f, indent=4, ensure_ascii=False)
            f.close()


def pre_process_all_files():
    for source in ['20Minutos', 'elMundo', 'elPais']:
        for category in ['ciencia', 'salud', 'tecnologia']:
            dir_path = '../data/' + source + '/' + category + '/'
            for file in os.listdir(dir_path):
                filepath = dir_path + file
                pre_process_file(filepath)


def compute_tf(processed_tokens):
    total_words = len(processed_tokens)

    df = pd.DataFrame(columns=['words', 'values'])
    fr = FreqDist(processed_tokens)

    i = 0
    for word, value in fr.items():
        df.loc[i] = [word, value]
        i = i + 1

    for i in range(len(df)):
        df['values'][i] = df['values'][i] / total_words

    return df


def compute_idf(processed_tokens):
    total_words = len(processed_tokens)

    df = pd.DataFrame(columns=['words', 'values'])
    fr = FreqDist(processed_tokens)

    i = 0
    for word, value in fr.items():
        df.loc[i] = [word, value]
        i = i + 1

    for i in range(len(df)):
        df['values'][i] = math.log(total_words / df['values'][i])

    return df


if __name__ == '__main__':
    # with open('../data/test.json', 'r') as f:
    #     js = json.load(f)

    # pre_process_file('../data/test.json')

    pre_process_all_files()

    # pr = pre_processing(js['content'])
    # print(pr)
    #
    # df = compute_tf(pr)
    # print(df)
