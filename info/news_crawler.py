import os
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup


def collect_news():
    result = []

    url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EC%B2%AD%EC%95%BD&oquery=%EC%B2%AD%EC%95%BD%EC%86%8C%EC%8B%9D&tqi=hA4RMdprvxZssKc1mjwssssstmK-352340'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # web_page_link_root = "https://search.naver.com"
    list_items = soup.select(".news_wrap")

    for item in list_items:
        # print(item)
        # title
        title = item.find("a", "news_tit").get_text()
        #
        # # body
        body = item.find("a", "api_txt_lines").get_text()
        #
        # # link
        link = item.find("a", "api_txt_lines").get('href')
        #
        result.append({
            'title': title,
            'body': body,
            'link': link
        })

    return result
