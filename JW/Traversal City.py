#-*- coding: UTF-8 -*-
#遍历所有城市，目的是为了获得城市，然后输出list，为后续自动化做准备
#原理：利用正则表达式来匹配符合要求的地址
import urllib.request
import re

url = "http://www.jiwu.com"
# 输出网址，输出页面代码
def get_WebPage(url):
    WebPageUrl = urllib.request.urlopen(url)
    WebPage = WebPageUrl.read().decode("utf8")
    WebPageUrl.close()
    # print(WebPage)
    return WebPage


# get_WebPage(url)


# 匹配所有jiwu.com结尾的网址，数据来源 上一个函数，非贪婪模式
city_list = re.findall('http://[^\s]*jiwu.com',get_WebPage(url),re.S)

#数据去重
city_list = list(set(city_list))


print(city_list)
# print(city_list)

# help(re)