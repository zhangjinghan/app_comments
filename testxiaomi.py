#coding=utf-8
from selenium import webdriver

import time

import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

opt = webdriver.ChromeOptions() #创建浏览器

# opt.set_headless() #无窗口模式

driver = webdriver.Chrome(options=opt) #创建浏览器对象

try:
    driver.get('https://www.baidu.com')#访问网址
    # input = driver.find_element_by_id(By.ID, 'kw')
    driver.find_element(By.ID, 'kw').send_keys('Python')
    # input.send_keys('Python')#在键盘里输入python
    input.send_keys(Keys.ENTER)#输入回车
    wait = WebDriverWait(driver, 10)#等待10秒
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))#等待ID为content_left加载出来
    print(driver.current_url)
    print(driver.get_cookies())
    print(driver.page_source)#源代码
finally:
    driver.close()


# driver.get('https://app.diandian.com/app/4xdipugo06l8sly/android-review') #打开网页

# # driver.maximize_window() #最大化窗口

# time.sleep(2) #加载等待



# # driver.find_element_by_xpath("./*//span[@class='bg s_ipt_wr quickdelete-wrap']/input").send_keys("魅族") #利用xpath查找元素进行输入文本
# driver.find_element_by_class_name("content")

# driver.find_element_by_id('kw').send_keys("小米") #候选方法



# driver.find_element_by_xpath("//span[@class='bg s_btn_wr']/input").click()#点击按钮

# driver.find_element_by_xpath("//input[@value='百度一下']").click()#候选方法

# driver.find_element_by_xpath("//span[@class='bg s_btn_wr']/input[type='submit'][value='百度一下']").click()#候选方法,多条件匹配