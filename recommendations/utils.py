# -*- encoding: utf-8 -*-

import pandas as pd
import os

from files import utils as jsutils


def similarity(tag_doc1, tag_doc2):
    if tag_doc1 == tag_doc2:
        return 1.0
    else:
        num = 2 * len(set(tag_doc1).intersection(tag_doc2))
        den = len(tag_doc1) + len(tag_doc2)
        return num / den


def all_sim(article, sources, categories):
    df = pd.DataFrame(columns=['file', 'title', 'similarity', 'percent'])

    article_title, article_tags = jsutils.read_title_tags(article)

    for source in sources:
        for category in categories:
            dir_path = './data/' + source + '/' + category + '/'
            for file in os.listdir(dir_path):
                filepath = dir_path + file
                if filepath != article:  # no hacer la compracion con el mismo
                    title, tags = jsutils.read_title_tags(filepath)
                    sim = similarity(article_tags, tags)
                    if sim >= 0.10:
                        percent = str(round(sim * 100, 2))
                        df.loc[-1] = [filepath, title, sim, percent]
                        df.index = df.index + 1

    return jsutils.reset_df(df, ['similarity', 'title'])
