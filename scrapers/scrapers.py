# -*- encoding: utf-8 -*-
import json
from datetime import datetime

import requests
from bs4 import BeautifulSoup


def scraper_elMundo(page):
    if page is "ciencia" or page is "salud":
        url = "https://www.elmundo.es/ciencia-y-salud/" + page
    else:
        url = "https://www.elmundo.es/tecnologia"

    page = requests.get(url + ".html")
    soup = BeautifulSoup(page.content, features='html.parser')

    for article in soup.find_all('article'):
        for a in article.find_all('a'):
            hrefs = a['href'].split('/')
            if 'ancla_comentarios' not in a['href'].split('#') \
                    and 'promociones' not in hrefs \
                    and 'album' not in hrefs:
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
                    'content': article_content
                }

                print(json.dumps(article_json, indent=4, ensure_ascii=False))
