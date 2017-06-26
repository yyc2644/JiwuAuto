#-*- coding: UTF-8 -*-
#示例代码，先以一个城市为原型抓去数据

#遍历所有城市，目的是为了获得城市，然后输出list，为后续自动化做准备
#原理：利用正则表达式来匹配符合要求的地址
import urllib.request
from bs4 import BeautifulSoup


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



# if __name__ == "__main__":


