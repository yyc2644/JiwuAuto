#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

'''
#遍历所有城市，目的是为了获得城市，然后输出list，为后续自动化做准备
#原理：利用正则表达式来匹配符合要求的地址
'''

__author__ = 'YiCheng'


import urllib.request
from bs4 import BeautifulSoup
import re

#未来改进的时候，多进程可能会用到Queue
'''
#re不会用，先拿beautifulsoup凑数
url = "http://cs.jiwu.com"

WebPageUrl = urllib.request.urlopen(url)

WebPage = WebPageUrl.read().decode("utf8")

#获取链接
url_list = re.findall('href=\"(.*?)\"', WebPage, re.S)

print(url_list)
url_all = []

for url in url_list:
    if "http" in url:
        print(url)
        url_all.append(url)

'''

# url = "http://cs.jiwu.com"
# def get_WebPage(url):
#     WebPageUrl = urllib.request.urlopen(url)
#     WebPage = WebPageUrl.read().decode("utf8")
#     WebPageUrl.close()
#     # print(WebPage)
#     return WebPage
#
# soup = BeautifulSoup(get_WebPage(url), "html.parser")
#
# #图片链接
# img = soup.find_all('a')
# # print(img)
#
# # img_list = re.findall("[a-zA-z]+://[^\s]*",img,re.S)
#
# # print(get_WebPage(url))


def get_url():
    url = "http://cs.jiwu.com"
    data=urllib.request.urlopen(url).read()
    page_data=data.decode("utf8")
    soup = BeautifulSoup(page_data, "html.parser")

    for link in soup.find_all('a'):
        print(link.get('href'))

    city_list = list(set(link.get('href')))


    return city_list

# help(re)
if __name__ == "__main__":

    get_url()
