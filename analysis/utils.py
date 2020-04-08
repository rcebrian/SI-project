import json

from nltk import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer

with open('../data/stopwords-es.json', 'r') as f:
    stop_js = json.load(f)
    ES_STOPWORDS = stop_js['words']


def preprocess(data):
    # tokenize and remove punctuation marks
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(data.lower())

    # apply stop words list
    for token in tokens:
        if token in ES_STOPWORDS:
            tokens.remove(token)

    # apply stemmer
    stemmer = SnowballStemmer('spanish')
    stemmed_tokens = []
    for token in tokens:
        stemmed_tokens.append(stemmer.stem(token))


if __name__ == '__main__':
    with open('../data/test.json', 'r') as f:
        js = json.load(f)

    preprocess(js['content'])
