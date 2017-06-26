#-*- coding: UTF-8 -*-
#示例代码，先以一个城市为原型抓去数据

#-*- coding: UTF-8 -*-
#遍历所有城市，目的是为了获得城市，然后输出list，为后续自动化做准备
#原理：利用正则表达式来匹配符合要求的地址
import urllib.request
import re

#未来改进的时候，多进程可能会用到Queue

'''
废弃代码
'''
# def get_WebPage(url):
#     WebPageUrl = urllib.request.urlopen(url)
#     WebPage = WebPageUrl.read().decode("utf8")
#     WebPageUrl.close()
#     return WebPage
#将得到的数据变更成适合存入数据库的样式
# def Forma_change():
# #匹配所有jiwu.com结尾的网址，数据来源 上一个函数，非贪婪模式
#
#     city_list = re.findall('http://\w*.\w*.\w*.\w*',get_WebPage(url))
# #数据去重
#     city_list = list(set(city_list))
#
#     return city_list

from selenium import webdriver

# driver = webdriver.Chrome("/Applications/chromedriver")
# driver.get("http://cs.jiwu.com")
# page = driver.page_source
# print page

#打开网页
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


if __name__ == "__main__":

    print("-------",url_all,"--------------",url_list)

