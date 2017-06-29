#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

'''
将获得url和解析同时放在这里运行
'''
__author__ = 'YiCheng'


def get_url():
    url = "http://cs.jiwu.com"
    data=urllib.request.urlopen(url).read()
    page_data=data.decode("utf8")
    soup = BeautifulSoup(page_data, "html.parser")

    for link in soup.find_all('a'):
        print(link.get('href'))

    city_list = list(set(link.get('href')))


    return link