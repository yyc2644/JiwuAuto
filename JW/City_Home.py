#-*- coding: UTF-8 -*-
#示例代码，先以一个城市为原型抓去数据

#-*- coding: UTF-8 -*-
#遍历所有城市，目的是为了获得城市，然后输出list，为后续自动化做准备
#原理：利用正则表达式来匹配符合要求的地址
import urllib.request
import re

#未来改进的时候，多进程可能会用到Queue


url = "http://cs.jiwu.com"
# 输出网址，输出网址
def get_WebPage(url):
    WebPageUrl = urllib.request.urlopen(url)
    WebPage = WebPageUrl.read().decode("utf8")
    WebPageUrl.close()
    return WebPage
#将得到的数据变更成适合存入数据库的样式
def Forma_change():
#匹配所有jiwu.com结尾的网址，数据来源 上一个函数，非贪婪模式
    city_list = re.findall('http://\w*.\w*.\w*.\w*[^a-zA-Z0-9]',get_WebPage(url))
#数据去重
    city_list = list(set(city_list))

    return city_list



if __name__ == "__main__":

    print(Forma_change())

