#-*- coding: UTF-8 -*-
# coding: UTF-8
#demo：https://blog.imdst.com/pythonzhong-yong-pycurljian-kong-httpxiang-ying-shi-jian-jiao-ben/

from io import StringIO
import pycurl
import sys
import os
import json

class Http_Test():
    #直接拷贝别人家的代码，不知道这个类有什么用
    def __init__(self):
        self.contents = ""
    def body_callback(self,buf):
        # self.contents = self.contents + buf
        pass




def Check_Url(input_url):
    #基本设置
    t = Http_Test()
    c = pycurl.Curl()
    c.setopt(pycurl.WRITEFUNCTION,t.body_callback)
    c.setopt(pycurl.ENCODING, 'gzip')
    c.setopt(pycurl.URL,input_url)
    c.perform()
    #定义需要监控的数据，目前只需要响应代码和链接时间
    http_code = c.getinfo(pycurl.HTTP_CODE)                             #响应代码
    http_conn_time = c.getinfo(pycurl.CONNECT_TIME)                     #连接时间
    http_pre_tran = c.getinfo(pycurl.PRETRANSFER_TIME)                  #连接上后到开始传输时间
    http_start_tran = c.getinfo(pycurl.STARTTRANSFER_TIME)              #接收到第一个字节的时间
    http_total_time = c.getinfo(pycurl.TOTAL_TIME)                      #域名解析时间
    http_size = c.getinfo(pycurl.SIZE_DOWNLOAD)                         #请求总的时间
    http_namelookup_time = c.getinfo(pycurl.NAMELOOKUP_TIME)            #域名解析时间
    http_connectcode = c.getinfo(pycurl.HTTP_CONNECTCODE)               #连接代码
    #输出模版
    info = """
            监测URL：%s
            响应代码: %s
            连接时间: %.3f秒
            域名解析时间: %.3f秒
            请求总的时间: %.3f秒
    """ \
           %(
            input_url,
            http_code,
            http_conn_time,
            http_namelookup_time,
            http_total_time
           )
    return info

if __name__ == "__main__":
    input_url = "http://cs.jiwu.com"
    info = Check_Url(input_url)
    print(info)