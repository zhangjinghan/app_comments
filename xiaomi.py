from typing_extensions import Self
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#   该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false        
def isElementExist(self,element):
    flag=True
    browser=self.driver
    try:
        browser.find_element_by_css_selector(element)
        return flag
    
    except:
        flag=False
        return flag

driver = webdriver.Chrome()

driver.get("https://app.diandian.com/app/6njqcmu6xj0rip4/android-review?market=3&summer=")



table=driver.find_element(By.CSS_SELECTOR,'#commentContent > div.loading-wrap > div > div > div > table')#定位网页表格位置
#获取表格包含的行，并将行数赋值
table_rows=table.find_elements(By.CSS_SELECTOR,'#commentContent > div.loading-wrap > div > div > div > table > tbody > tr')# table包含行数的集合，包含标题
print('table_rows',table_rows)

vrows=len(table_rows)-1#将总行数赋给变量
print('vrows',vrows)
#table_cols=table_rows[0].find_elements_by_tag_name('th')# tabler的总列数
#遍历每行第2列（by_tag_name('td')[1]）的值，也可以获取其他列只需要将[1]更改为需要获取的列即可。
for table_num in range(1, vrows):
    time.sleep(2)
    # table_text=table_rows[table_num].find_elements(By.CSS_SELECTOR,'#commentContent > div.loading-wrap > div > div > div > table > tbody > tr > td > div > div > div.dd-word-wrap > div > p > span')#遍历每行第2列获取单元格的值。
    # for e in table_text:
    #     print(e.text)


    driver.implicitly_wait(6)
    time.sleep(2)
    content = driver.find_element(by=By.CSS_SELECTOR, value="#commentContent > div.loading-wrap > div > div > div > table > tbody > tr:nth-child("+str(table_num)+") > td:nth-child(2) > div > div > div.dd-word-wrap > div > p > span").text
    print('content:',content)                               #commentContent > div.loading-wrap > div > div > div > table > tbody > tr:nth-child(8) > td:nth-child(2) > div > div > div.dd-word-wrap > div > p > span
                                                            #commentContent > div.loading-wrap > div > div > div > table > tbody > tr:nth-child(6) > td:nth-child(2) > div > div > div.dd-word-wrap > div > p > span
    driver.implicitly_wait(6)
    time.sleep(2)
    score = driver.find_element(by=By.CSS_SELECTOR, value="#commentContent > div.loading-wrap > div > div > div > table > tbody > tr:nth-child("+str(table_num)+") > td:nth-child(1) > div.dd-table-cell > div > div").get_attribute("aria-valuenow")
    print('score:',score)                            


    driver.implicitly_wait(10)
    time.sleep(2)
    date = driver.find_element(by=By.CSS_SELECTOR, value="#commentContent > div.loading-wrap > div > div > div > table > tbody > tr:nth-child("+str(table_num)+") > td:nth-child(3) > div > div").text
    print('date:',date)



    version = driver.find_element(by=By.CSS_SELECTOR, value="#commentContent > div.loading-wrap > div > div > div > table > tbody > tr:nth-child("+str(table_num)+") > td:nth-child(2) > div > div > div.comment-info.dd-flex.dd-flex-warp > span:nth-child(6)")
    version_live = isElementExist(Self,version)
    print(version_live)  
    if(version_live!=0):
        print(version.text) 
                                            #commentContent > div.loading-wrap > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > div > div > div.comment-info.dd-flex.dd-flex-warp > span:nth-child(6)
                                            #commentContent > div.loading-wrap > div > div > div > table > tbody > tr:nth-child(3) > td:nth-child(2) > div > div > div.comment-info.dd-flex.dd-flex-warp > span:nth-child(6)

driver.implicitly_wait(0.5)
# elements = driver.find_elements(by=By.TAG_NAME,value='table')


# version = driver.find_elements(by=By.CSS_SELECTOR, value="#commentContent > div.loading-wrap > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > div > div > div.comment-info.dd-flex.dd-flex-warp > span:nth-child(6)")
# for e in version:
#     print(e.text)
# date = driver.find_element(by=By.CSS_SELECTOR, value="#commentContent > div.loading-wrap > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > div").text
# for e in date:
#     print(e.text)
# username = driver.find_elements(by=By.CSS_SELECTOR, value="#commentContent > div.loading-wrap > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > div > div > div.comment-info.dd-flex.dd-flex-warp > div > a")
# for e in username:
#     print(e.text)

# next_button = driver.find_element(by=By.CSS_SELECTOR, value="#commentContent > div.loading-wrap > div > div > div > div > div > button.btn-next")

# # print(content)
# # print(score)
# # print(version)
# # print(date)
# # print(username)


# next_button.click()

# search_box = driver.find_element(by=By.NAME, value="q")
# value = search_box.get_attribute("value")
# assert value == "Selenium"

# driver.quit()

