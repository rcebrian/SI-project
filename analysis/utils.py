import json
import math
import os

import pandas as pd
from nltk import RegexpTokenizer, FreqDist
from nltk.stem.snowball import SnowballStemmer

with open('./data/stopwords-es.json', 'r') as f:
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
            dir_path = './data/' + source + '/' + category + '/'
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


def compute_idf_tokens(sources, categories):
    stemmed_tokens = []

    for source in sources:  # ['20Minutos', 'elMundo', 'elPais']:
        for category in categories:  # ['ciencia', 'salud', 'tecnologia']:
            dir_path = './data/' + source + '/' + category + '/'
            for file in os.listdir(dir_path):
                filepath = dir_path + file
                with open(filepath, 'r') as f:
                    js = json.load(f)
                    for token in js['processed']:
                        stemmed_tokens.append(token)
                    f.close()
    df = compute_idf(stemmed_tokens)
    return df


def compute_tf_idf(df_tf, df_idf):
    df_tf_idf = pd.DataFrame(columns=['words', 'values'])
    for i in range(len(df_tf)):
        df_tf_idf.loc[i] = [df_tf['words'][i], df_tf['values'][i] * df_idf['values'][i]]
    return df_tf_idf


def cosine_formula(df_tf_idf, df_tf_idf_query):
    numerator = sum(df_tf_idf['values'] * df_tf_idf_query['values'])

    sum_file = 0
    sum_query = 0
    for j in range(len(df_tf_idf)):
        sum_file = sum_file + pow(df_tf_idf['values'][j], 2)
        sum_query = sum_query + pow(df_tf_idf_query['values'][j], 2)

    denominator = math.sqrt(sum_file) * math.sqrt(sum_query)
    if denominator is 0:
        return 0
    else:
        return numerator / denominator


def query_similarity(sources, categories, total_idf, query_tf_idf, top):
    stemmed_tokens = []
    json_files = []
    df_idf1 = pd.DataFrame(columns=['words', 'values'])
    df_sim = pd.DataFrame(columns=['file', 'similarity'])

    # remove unnecessary tokens
    for i in range(len(query_tf_idf)):
        if query_tf_idf['words'][i] in total_idf['words'].values:
            df_idf1 = df_idf1.append(total_idf[total_idf['words'] == query_tf_idf['words'][i]])
        else:
            df_idf1.loc[i] = [query_tf_idf['words'][i], 0]
    df_idf1.reset_index(inplace=True)
    del df_idf1['index']

    # save all stemmed tokens and filename
    for source in sources:
        for category in categories:
            dir_path = './data/' + source + '/' + category + '/'
            for file in os.listdir(dir_path):
                filepath = dir_path + file
                with open(filepath, 'r') as f:
                    js = json.load(f)
                    json_files.append(filepath)
                    stemmed_tokens.append(js['processed'])
                    f.close()

    for s in range(len(stemmed_tokens)):
        tf = compute_tf(stemmed_tokens[s])
        df_tf = pd.DataFrame(columns=['words', 'values'])

        # remove unnecessary tokens
        for i in range(len(query_tf_idf)):
            if query_tf_idf['words'][i] in tf['words'].values:
                df_tf = df_tf.append(tf[tf['words'] == query_tf_idf['words'][i]])
            else:
                df_tf.loc[i] = [query_tf_idf['words'][i], 0]
        df_tf.reset_index(inplace=True)
        del df_tf['index']

        token_tf_idf = compute_tf_idf(df_tf=df_tf, df_idf=df_idf1)
        sim = cosine_formula(df_tf_idf=token_tf_idf, df_tf_idf_query=query_tf_idf)

        if len(df_sim) < top:
            df_sim.loc[len(df_sim)] = [json_files[s], sim]
        else:
            if any(z < sim for z in df_sim['similarity'].values):
                pos = df_sim[df_sim['similarity'] == df_sim['similarity'].min()].index[0]
                df_sim.loc[pos] = [json_files[s], sim]

    # order by DES and reset index
    df_sim = df_sim.sort_values('similarity', ascending=False)
    df_sim.reset_index(inplace=True)
    del df_sim['index']

    return df_sim


def get_query_tf_idf(query):
    tf = compute_tf(pre_processing(query))
    idf = compute_idf(pre_processing(query))
    query_tf_idf = compute_tf_idf(df_tf=tf, df_idf=idf)
    return query_tf_idf


def total_idf(sources, categories):
    return compute_idf_tokens(sources, categories)
