# -*- encoding: utf-8 -*-
import json
import os
from datetime import datetime

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
    path = "../data/" + directory + "/" + category + "/"
    dates = []

    exist = False

    for js in os.listdir(path):
        if content['date'] in js:
            if article_exists(path + js, content):
                exist = True
            dates.append(int(js.split('.')[-2]))
    if len(dates) is 0:
        a_id = 1
    else:
        dates.sort()
        a_id = dates[-1] + 1

    print(exist)
    if not exist:
        path = "../data/" + directory + "/" + category + "/" + category + "." + content['date'] + '.{0:0>3}'.format(
            a_id) + ".json"
        print('> Writing file: ', path)
        with open(path, 'w') as f:
            json.dump(content, f, indent=4, ensure_ascii=False)


def scraper_elMundo(category):
    if category is "ciencia" or category is "salud":
        url = "https://www.elmundo.es/ciencia-y-salud/" + category
    else:
        url = "https://www.elmundo.es/tecnologia"

    page = requests.get(url + ".html")
    soup = BeautifulSoup(page.content, features='html.parser')

    for article in soup.find_all('article'):
        for a in article.find_all('a'):
            hrefs = a['href'].split('/')
            if 'ancla_comentarios' not in a['href'].split('#') and 'promociones' not in hrefs and 'album' not in hrefs:
                page_article = requests.get(a['href'])
                soup_article = BeautifulSoup(page_article.content, features='html.parser')

                article_title = soup_article.find('h1').get_text()
                article_subtitle = soup_article.find('p', class_='ue-c-article__standfirst').get_text()
                article_author = soup_article.find('div', class_='ue-c-article__byline-name').get_text()
                article_datetime = soup_article.find('time')['datetime']
                article_date = datetime.strptime(article_datetime, "%Y-%m-%dT%H:%M:%SZ").strftime('%Y-%m-%d')
                article_time = datetime.strptime(article_datetime, "%Y-%m-%dT%H:%M:%SZ").strftime('%H:%M')
                article_content = ""
                content = soup_article.find('div', class_='ue-l-article__body ue-c-article__body')
                for p_tag in content.find_all('p', recursive=False):
                    article_content += p_tag.get_text()

                article_json = {
                    'title': article_title,
                    'subtitle': article_subtitle,
                    'author': article_author,
                    'date': article_date,
                    'time': article_time,
                    'content': article_content,
                    'processed': None
                }
                store_data('elMundo', category, article_json)


def scraper_elPais(category):
    # switch category
    if category is "tecnologia" or category is "ciencia":
        url = "https://elpais.com/" + category + "/"
    else:
        url = "https://elpais.com/noticias/" + category + "/"

    if category is "sanidad":
        category = "salud"

    # get page response
    page = requests.get(url)
    soup = BeautifulSoup(page.content, features='html.parser')

    # get articles from category page
    for article in soup.find_all('article', class_='story_card'):
        for a in article.find_all('a'):
            hrefs = a['href'].split('/')
            if "autor" not in hrefs and \
                    "hemeroteca" not in hrefs and \
                    "actualidad" not in hrefs and \
                    "https:" not in hrefs and \
                    "elpais" not in hrefs:  # remove video links
                print(a['href'])
                page_article = requests.get("https://elpais.com" + a['href'])
                soup_article = BeautifulSoup(page_article.content, features='html.parser')

                article_content = ""
                content = soup_article.find('div', class_='article_body')

                article_title = soup_article.find('h1').get_text()
                article_subtitle = soup_article.find('h2').get_text()
                try:
                    article_author = soup_article.find('a', class_='color_black').get_text()
                except:
                    article_author = soup_article.find('span',
                                                       class_='margin_bottom uppercase flex align_items_center margin_right').get_text()
                article_date = soup_article.find('div', class_='place_and_time').find('a')['href'].split('/')[-2]
                article_time = \
                    soup_article.find('div', class_='place_and_time').find('a', recursive=False).get_text().split('-')[
                        -1].strip()  # todo: fix time error UTC+1

                for p_tag in content.find_all('p', recursive=False):
                    article_content = p_tag.get_text()

                article_json = {
                    'title': article_title,
                    'subtitle': article_subtitle,
                    'author': article_author,
                    'date': article_date,
                    'time': article_time,
                    'content': article_content,
                    'processed': None
                }
                store_data('elPais', category, article_json)


def scraper_20minutos(category):
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
                    "noticia" in a['href'] and \
                    "#" not in a['href'] and \
                    "4220544" not in a['href'] and \
                    a['href'][0] is not "/":
                links.append(a['href'])
                page_article = requests.get(a['href'])
                soup_article = BeautifulSoup(page_article.content, features='html.parser')

                article_title = soup_article.find_all('h1')[-1].get_text()
                try:
                    article_subtitle = soup_article.find('div', class_='article-intro').find('li').get_text()
                except:
                    article_subtitle = soup_article.find('div', class_='article-intro').get_text()
                article_author = soup_article.find('span', class_='article-author').find('strong').get_text()

                article_datetime = soup_article.find('span', class_='article-date').find('a').get_text()
                article_date = datetime.strptime(article_datetime, "%d.%m.%Y - %H:%Mh").strftime('%Y-%m-%d')
                article_time = datetime.strptime(article_datetime, "%d.%m.%Y - %H:%Mh").strftime('%H:%M')

                article_content = ""
                content = soup_article.find('div', class_='article-text')
                for p_tag in content.find_all('p', class_='paragraph', recursive=False):
                    article_content += p_tag.get_text()

                article_json = {
                    'title': article_title,
                    'subtitle': article_subtitle,
                    'author': article_author,
                    'date': article_date,
                    'time': article_time,
                    'content': article_content,
                    'processed': None
                }
                store_data('20Minutos', category, article_json)


if __name__ == '__main__':
    # scraper_elMundo('ciencia')
    # scraper_elPais('ciencia')
    # scraper_elPais('sanidad')
    # scraper_elPais('tecnologia')
    # scraper_20minutos('salud')
    # scraper_20minutos('ciencia')
    scraper_20minutos('tecnologia')
