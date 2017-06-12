from selenium import webdriver

browser = webdriver.Chrome("/Applications/chromedriver")
browser.get("http://bj.jiwu.com/loupan/54410.html")

browser.find_element_by_id("mobile520").send_keys("13691712693")
browser.find_element_by_id("yzm520").send_keys("470515")



if 1==1:
    browser.find_element_by_class_name("getyzm").click()
