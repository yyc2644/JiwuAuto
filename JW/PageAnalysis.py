#-*- coding: UTF-8 -*-
# coding: UTF-8

from io import StringIO
import pycurl
import sys
import os
import json

class Http_Test():
    def __init__(self):
        self.contents = ""
    def body_callback(self,buf):
        # self.contents = self.contents + buf
        pass




def Check_Url(input_url):
    t = Http_Test()
    c = pycurl.Curl()
    c.setopt(pycurl.WRITEFUNCTION,t.body_callback)
    c.setopt(pycurl.ENCODING, 'gzip')
    c.setopt(pycurl.URL,input_url)
    c.perform()
    http_code = c.getinfo(pycurl.HTTP_CODE)
    http_conn_time = c.getinfo(pycurl.CONNECT_TIME)
    http_pre_tran = c.getinfo(pycurl.PRETRANSFER_TIME)
    http_start_tran = c.getinfo(pycurl.STARTTRANSFER_TIME)
    http_total_time = c.getinfo(pycurl.TOTAL_TIME)
    http_size = c.getinfo(pycurl.SIZE_DOWNLOAD)
    http_namelookup_time = c.getinfo(pycurl.NAMELOOKUP_TIME)
    http_connectcode = c.getinfo(pycurl.HTTP_CONNECTCODE)
    info = """
    监测URL：%s
    响应代码: %s
    连接代码: %s
    连接时间: %.3f秒
    域名解析时间: %.3f秒
    请求总的时间: %.3f秒
    连接上后到开始传输时间: %.3f秒
    接收到第一个字节的时间: %.3f秒
    """ %( input_url,http_code,http_connectcode,http_conn_time,http_namelookup_time,http_total_time,http_pre_tran,http_start_tran)
    return info

if __name__ == "__main__":
    input_url = "http://cs.jiwu.com"
    info = Check_Url(input_url)
    print(info)