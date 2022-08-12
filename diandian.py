# from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pymysql
from selenium.webdriver.chrome.options import Options

def myscrapy(urls,market,appname):
    
    ####################################
    # Linux版本需要加入option字段
    ch_options = webdriver.ChromeOptions()
    #为Chrome配置无头模式
    ch_options.add_argument("--headless")  
    ch_options.add_argument('--no-sandbox')
    ch_options.add_argument('--disable-gpu')
    ch_options.add_argument('--disable-dev-shm-usage')
    # 在启动浏览器时加入配置
    driver = webdriver.Chrome(options=ch_options)
    #####################################

    # driver = webdriver.Chrome()

    # 连接数据库
    db = pymysql.connect(
    host="127.0.0.1", 
    port=3306,
    user='root',    #在这里输入用户名
    password='root',     #在这里输入密码
    database='comments',
    charset='utf8mb4'
    )
    cursor = db.cursor() #创建游标对象

    # 删除表中数据
    sql='truncate table database_comments_'+str(appname)+';'
    cursor.execute(sql)   
    db.commit()

    for k,v in urls.items():
        driver.get("https://app.diandian.com/app/"+str(v)+"/android-review?market="+str(market)+"&summer=")
        # 爬前10页

        for i in range(10):
            print("i=",i,"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            # 点击下一页
            if (i!=0):
                #try处理部分应用只有一页评论，没有nextbutton按钮
                try:
                    next_button = driver.find_element(by=By.CSS_SELECTOR, value="#commentContent > div.loading-wrap > div > div > div > div > div > button.btn-next")
                    disable = next_button.get_attribute("disabled")
                    print(disable)
                    print(type(disable))
                    # 如果下一页可用
                    if(disable!='true'):
                        next_button.click()
                        print("next page")
                    else: 
                        print("没有点击下一页")
                        break
                except:
                    break
            # 开始爬表格数据
            time.sleep(2)
            table=driver.find_element(By.CSS_SELECTOR,'#commentContent > div.loading-wrap > div > div > div > table')#定位网页表格位置
            #获取表格包含的行，并将行数赋值
            time.sleep(2)
            table_rows=table.find_elements(By.CSS_SELECTOR,'#commentContent > div.loading-wrap > div > div > div > table > tbody > tr')# table包含行数的集合，包含标题
                                                        
            print('table_rows',table_rows)

            vrows=len(table_rows)#将总行数赋给变量
            print('vrows',vrows)

            for table_num in range(1, vrows):

                time.sleep(2)
                try:
                    content = driver.find_element(by=By.CSS_SELECTOR, value="#commentContent > div.loading-wrap > div > div > div > table > tbody > tr:nth-child("+str(table_num)+") > td:nth-child(2) > div > div > div.dd-word-wrap > div > p > span").text
                    print('content:',content)                             
                except:
                    continue  

                time.sleep(2)
                score = driver.find_element(by=By.CSS_SELECTOR, value="#commentContent > div.loading-wrap > div > div > div > table > tbody > tr:nth-child("+str(table_num)+") > td:nth-child(1) > div.dd-table-cell > div > div").get_attribute("aria-valuenow")
                print('score:',score)                            

                time.sleep(2)
                date = driver.find_element(by=By.CSS_SELECTOR, value="#commentContent > div.loading-wrap > div > div > div > table > tbody > tr:nth-child("+str(table_num)+") > td:nth-child(3) > div > div").text
                print('date:',date)

                try:
                    version = driver.find_element(by=By.CSS_SELECTOR, value="#commentContent > div.loading-wrap > div > div > div > table > tbody > tr:nth-child("+str(table_num)+") > td:nth-child(2) > div > div > div.comment-info.dd-flex.dd-flex-warp > span:nth-child(6)").text
                    print('version:',version)
                except:
                    version = " "
                    print("not found version!")

                time.sleep(2)
                try:
                    user = driver.find_element(by=By.CSS_SELECTOR, value="#commentContent > div.loading-wrap > div > div > div > table > tbody > tr:nth-child("+str(table_num)+") > td:nth-child(2) > div > div > div.comment-info.dd-flex.dd-flex-warp > div > a").text
                    print('user:',user)
                except:
                    user = "anoy"
                    print("not found user!")
                
                time.sleep(2)
                name = driver.find_element(by=By.CSS_SELECTOR, value=" #appinfo-content > div.container > div:nth-child(2) > div.content-side > div.container-head > div.dd-flex-1.dd-flex.dd-flex-column.dd-flex-space.dd-overflow-hidden > div.logo-wrap > div.max-width-80 > div.app-name > h1").text
                print('name:',name)

                data = [date,user,content,score,version,name]
                print(data)

                sql = 'insert into database_comments_'+str(appname) +'(date,user,content,score,version,name) values(%s,%s,%s,%s,%s,%s);'
                cursor.execute(sql,data)     # 插入数据
                db.commit()

    cursor.close() 
    db.close()  #关闭数据库连接
    driver.quit() # 退出浏览器

