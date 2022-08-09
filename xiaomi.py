from lib2to3.pgen2 import driver
from typing_extensions import Self
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://app.diandian.com/app/6njqcmu6xj0rip4/android-review?market=3&summer=")


def scrapy_table(flag):
    global driver
    # if flag == 0: 
    #     driver = webdriver.Chrome()
    #     driver.get("https://app.diandian.com/app/6njqcmu6xj0rip4/android-review?market=3&summer=")

    if flag == 1:
        next_button = driver.find_element(by=By.CSS_SELECTOR, value="#commentContent > div.loading-wrap > div > div > div > div > div > button.btn-next")
        next_button.click()

    table=driver.find_element(By.CSS_SELECTOR,'#commentContent > div.loading-wrap > div > div > div > table')#定位网页表格位置
    #获取表格包含的行，并将行数赋值
    table_rows=table.find_elements(By.CSS_SELECTOR,'#commentContent > div.loading-wrap > div > div > div > table > tbody > tr')# table包含行数的集合，包含标题
    print('table_rows',table_rows)

    vrows=len(table_rows)#将总行数赋给变量
    print('vrows',vrows)
    #table_cols=table_rows[0].find_elements_by_tag_name('th')# tabler的总列数
    #遍历每行第2列（by_tag_name('td')[1]）的值，也可以获取其他列只需要将[1]更改为需要获取的列即可。
    for table_num in range(1, vrows):

        time.sleep(2)
        try:
            content = driver.find_element(by=By.CSS_SELECTOR, value="#commentContent > div.loading-wrap > div > div > div > table > tbody > tr:nth-child("+str(table_num)+") > td:nth-child(2) > div > div > div.dd-word-wrap > div > p > span").text
            print('content:',content)                               #commentContent > div.loading-wrap > div > div > div > table > tbody > tr:nth-child(8) > td:nth-child(2) > div > div > div.dd-word-wrap > div > p > span
        except:
            continue                                                        #commentContent > div.loading-wrap > div > div > div > table > tbody > tr:nth-child(6) > td:nth-child(2) > div > div > div.dd-word-wrap > div > p > span
        driver.implicitly_wait(6)
        time.sleep(2)
        score = driver.find_element(by=By.CSS_SELECTOR, value="#commentContent > div.loading-wrap > div > div > div > table > tbody > tr:nth-child("+str(table_num)+") > td:nth-child(1) > div.dd-table-cell > div > div").get_attribute("aria-valuenow")
        print('score:',score)                            

        driver.implicitly_wait(10)
        time.sleep(2)
        date = driver.find_element(by=By.CSS_SELECTOR, value="#commentContent > div.loading-wrap > div > div > div > table > tbody > tr:nth-child("+str(table_num)+") > td:nth-child(3) > div > div").text
        print('date:',date)

        try:
            version = driver.find_element(by=By.CSS_SELECTOR, value="#commentContent > div.loading-wrap > div > div > div > table > tbody > tr:nth-child("+str(table_num)+") > td:nth-child(2) > div > div > div.comment-info.dd-flex.dd-flex-warp > span:nth-child(6)")
            print('version:',version.text)
        except:
            print("version: not found version！")


for i in range(10):
    if i == 0:
        flag = 0
    else: 
        flag = 1
    scrapy_table(flag)
# https://app.diandian.com/app/6njqcmu6xj0rip4/android-review?market=3&summer=




time.sleep(2)
# next_button = driver.find_element(by=By.CSS_SELECTOR, value="#commentContent > div.loading-wrap > div > div > div > div > div > button.btn-next")
# next_button.click()

# search_box = driver.find_element(by=By.NAME, value="q")
# value = search_box.get_attribute("value")
# assert value == "Selenium"

# driver.quit()

