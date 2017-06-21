#-*- coding: UTF-8 -*-
#示例代码，分析每个网页的服务器头文件，访问时间，访问状态等

import urllib.request
import pycurl


# with urllib.request.urlopen("https://cs.jiwu.com") as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))
#
# url = "http://cs.jiwu.com"
# page = urllib.request.urlopen(url)
#
# print(page.status)
# print(page.getheaders)
# print("aaa:",(page.read().decode('utf8')))
#
# a = pycurl.CONNECT_TIME

# # http_conn_time =  c.getinfo(pycurl.CONNECT_TIME)
# c = pycurl.Curl().getinfo(pycurl.URL, "http://cs.jiwu.com")
#
#
# c.setopt(pycurl.ENCODING, 'gzip')
#
# c.setopt(pycurl.URL, "http://cs.jiwu.com")
#
#
# http_conn_time = c.getinfo(pycurl.CONNECT_TIME)
#
# print(http_conn_time)

#
#
# c = pycurl.Curl()
# c.setopt(pycurl.URL, "http://cs.jiwu.com")
# c.setopt(pycurl.FOLLOWLOCATION, 1)
# # c.perform()
# print("connect",c.getinfo(pycurl.CONNECT_TIME),"url=",c.getinfo(pycurl.CURL_HTTP_VERSION_NONE))

# coding:utf-8
import unittest
import HTMLTestRunner

def all_case():
    # 待执行用例的目录
    case_dir = "D:\\test\\yoyotest\\case"
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,
                                                   pattern="test*.py",
                                                   top_level_dir=None)
    # discover方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            # 添加用例到testcase
            testcase.addTests(test_case)
    print(testcase)
    return testcase

if __name__ == "__main__":
    # 返回实例
    # runner = unittest.TextTestRunner()
    report_path = "D:\\test\\yoyotest\\report\\result.html"

    fp = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'这是我的自动化测试报告',
                                           description=u'用例执行情况：')

    # run所有用例  交流QQ群：232607095
    runner.run(all_case())
    fp.close()