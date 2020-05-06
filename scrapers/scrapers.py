# -*- encoding: utf-8 -*-
import json
import os
from datetime import datetime
import unidecode

import requests
from bs4 import BeautifulSoup


def article_exists(old, new):
    with open(old, 'r') as f:
        js = json.load(f)
    if js['date'] == new['date'] and js['time'] == new['time']:
        return True
    else:
        return False


def store_data(directory, category, content):
    path = "./data/" + directory + "/" + category + "/"
    dates = []

    exist = False

    for js in os.listdir(path):
        if content['date'] in js:
            if article_exists(path + js, content):
                exist = True
            dates.append(int(js.split('.')[-2]))
    if len(dates) == 0:
        a_id = 1
    else:
        dates.sort()
        a_id = dates[-1] + 1

    print(exist)
    if not exist:
        path = "./data/" + directory + "/" + category + "/" + category + "." + content['date'] + '.{0:0>3}'.format(
            a_id) + ".json"
        print('> Writing file: ', path)
        with open(path, 'w') as f:
            json.dump(content, f, indent=4, ensure_ascii=False)


def scraper_elMundo(categories):
    for category in categories:
        if category == "ciencia" or category == "salud":
            url = "https://www.elmundo.es/ciencia-y-salud/" + category
        else:
            url = "https://www.elmundo.es/tecnologia"

        page = requests.get(url + ".html")
        soup = BeautifulSoup(page.content, features='html.parser')

        for article in soup.find_all('article'):
            for a in article.find_all('a'):
                if 'ancla_comentarios' not in a['href'] and \
                        'promociones' not in a['href'] and \
                        'album' not in a['href'] and \
                        '.html' in a['href']:
                    page_article = requests.get(a['href'])
                    soup_article = BeautifulSoup(page_article.content, features='html.parser')
                    tags = []
                    processed_tags = []
                    article_datetime = soup_article.find('time')['datetime']
                    article_content = ""
                    content = soup_article.find('div', class_='ue-l-article__body ue-c-article__body')

                    try:
                        soup_author = soup_article.find('div', class_='ue-c-article__byline-name').get_text()
                    except:
                        soup_author = None

                    for p_tag in content.find_all('p', recursive=False):
                        article_content += p_tag.get_text() + "\n"

                    for tag in soup_article.find_all('li', class_='ue-c-article__tags-item'):
                        tg = tag.get_text()
                        tags.append(tg)
                        processed_tags.append(unidecode.unidecode(tg.lower()))

                    article_json = {
                        'title': soup_article.find('h1').get_text(),
                        'subtitle': soup_article.find('p', class_='ue-c-article__standfirst').get_text(),
                        'author': soup_author,
                        'date': datetime.strptime(article_datetime, "%Y-%m-%dT%H:%M:%SZ").strftime('%Y-%m-%d'),
                        'time': datetime.strptime(article_datetime, "%Y-%m-%dT%H:%M:%SZ").strftime('%H:%M'),
                        'content': article_content,
                        'tags': tags,
                        'processed_tags': processed_tags,
                        'processed': None
                    }
                    store_data('elMundo', category, article_json)
                    # print(json.dumps(article_json, indent=4, ensure_ascii=False))


def scraper_elPais(categories):
    for category in categories:
        # switch category
        if category == "tecnologia" or category == "ciencia":
            url = "https://elpais.com/" + category + "/"
        else:
            category = "sanidad"
            url = "https://elpais.com/noticias/" + category + "/"

        if category == "sanidad":
            category = "salud"

        # get page response
        page = requests.get(url)
        soup = BeautifulSoup(page.content, features='html.parser')

        for article in soup.find_all('article', class_='story_card'):
            for a in article.find_all('a'):
                if "https" not in a['href'] and \
                        "album" not in a['href'] and \
                        "hemeroteca" not in a['href']:
                    page_article = requests.get("https://elpais.com" + a['href'])
                    soup_article = BeautifulSoup(page_article.content, features='html.parser')

                    tags = []
                    processed_tags = []

                    try:
                        article_date = soup_article.find('a', class_='a_ti')['href'].split('/')[-2]
                        article_time = soup_article.find('div', {'class': ['place_and_time', 'a_pt']}).find('a',
                                                                                                            recursive=False).get_text().split(
                            '-')[-1].strip()[0:5]
                    except:
                        article_datetime = soup_article.find('time')['datetime']
                        article_date = article_datetime.split('T')[0]
                        article_time = article_datetime.split('T')[1].split('+')[0][0:5]

                    try:
                        article_author = soup_article.find('div',
                                                           {'class': ['a_auts', 'autor-texto']}).get_text().strip()
                    except:
                        article_author = None  # publi (example: https://elpais.com/tecnologia/2020/03/09/actualidad/1583773553_899599.html)

                    for tag in soup_article.find_all('meta', property='article:tag'):
                        tg = tag['content']
                        tags.append(tg)
                        processed_tags.append(unidecode.unidecode(tg.lower()))

                    article_content = ""
                    for p_tag in soup_article.find('div', {'class': ['article_body', 'articulo-cuerpo']}).find_all('p',
                                                                                                                   recursive=False):
                        article_content += p_tag.get_text() + "\n"

                    article_json = {
                        'title': soup_article.find('h1', {'class': ['a_t', 'articulo-titulo']}).get_text(),
                        'subtitle': soup_article.find('h2', {'class': ['a_st', 'articulo-subtitulo']}).get_text(),
                        'author': article_author,
                        'date': article_date,
                        'time': article_time,
                        'content': article_content,
                        'tags': tags,
                        'processed_tags': processed_tags,
                        'processed': None
                    }
                    store_data('elPais', category, article_json)
                    # print(json.dumps(article_json, indent=4, ensure_ascii=False))


def scraper_20minutos(categories):
    for category in categories:
        # switch category
        url = "https://20minutos.es/" + category + "/"

        # get page response
        page = requests.get(url)
        soup = BeautifulSoup(page.content, features='html.parser')
        links = []

        # get articles from category page
        for article in soup.find_all('article', class_='media'):
            for a in article.find_all('a'):
                if a['href'] not in links and \
                        "https" in a['href'] and \
                        "noticia" in a['href'] and \
                        "4203956" not in a['href'] and \
                        "4220544" not in a['href'] and \
                        "4222535" not in a['href'] and \
                        "undefined" not in a['href']:
                    links.append(a['href'])  # saved to avoid duplicates
                    page_article = requests.get(a['href'])
                    soup_article = BeautifulSoup(page_article.content, features='html.parser')

                    tags = []
                    processed_tags = []
                    # subtitle
                    try:
                        article_subtitle = soup_article.find('div', class_='article-intro').find('li').get_text()
                    except:
                        article_subtitle = None

                    # author
                    try:
                        article_author = soup_article.find('span', class_='article-author').find('strong').get_text()
                    except:
                        article_author = None

                    # date
                    try:
                        article_datetime = soup_article.find('span', class_='article-date').find('a').get_text()
                        article_date = datetime.strptime(article_datetime, "%d.%m.%Y - %H:%Mh").strftime('%Y-%m-%d')
                        article_time = datetime.strptime(article_datetime, "%d.%m.%Y - %H:%Mh").strftime('%H:%M')
                    except:
                        article_date = None
                        article_time = None

                    for tag in soup_article.find_all('li', class_='tag'):
                        ta = tag.find('a').get_text().strip()
                        tags.append(ta)
                        processed_tags.append(unidecode.unidecode(ta.lower()))

                    article_content = ""
                    content = soup_article.find('div', class_='article-text')
                    for p_tag in content.find_all('p', class_='paragraph', recursive=False):
                        article_content += p_tag.get_text() + "\n"

                    article_json = {
                        'title': soup_article.find('h1').get_text(),
                        'subtitle': article_subtitle,
                        'author': article_author,
                        'date': article_date,
                        'time': article_time,
                        'content': article_content,
                        'tags': tags,
                        'processed_tags': processed_tags,
                        'processed': None
                    }
                    store_data('20Minutos', category, article_json)
                    # print(json.dumps(article_json, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    scraper_elMundo(['tecnologia', 'ciencia', 'salud'])
