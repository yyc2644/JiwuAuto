#-*- coding: UTF-8 -*-
#遍历所有城市，目的是为了获得城市，然后输出list，为后续自动化做准备
#原理：利用正则表达式来匹配符合要求的地址
from selenium import webdriver
import re

driver =  webdriver.Chrome("/Applications/chromedriver")
driver.get("http://www.jiwu.com/")
page = driver.page_source
# print(page)


#非贪婪模式，re.s（'.'匹配字符，包括换行）
city_list = re.findall('[a-zA-z]+://[^\s]*com',page,re.S)
re_rule = "(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?"
# city_list = re.findall(re_rule,page)
# print(city_list)
for clist in  city_list:
    print(clist)

# print(city_list)