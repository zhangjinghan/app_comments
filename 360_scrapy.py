from codecs import unicode_escape_decode, utf_8_decode
from xml.etree.ElementTree import Comment
from numpy import unicode_
import requests
from bs4 import BeautifulSoup
import json
import time
from timeloop import Timeloop
from  datetime import timedelta
import pymysql

headers = {
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

# 定时模块
tl = Timeloop()
@tl.job(interval=timedelta(seconds=600))
def sample_job_every_600s():
    # 连接数据库
    db = pymysql.connect(
    
    host="127.0.0.1", 
    port=3306,
    user='root',    #在这里输入用户名
    password='root',     #在这里输入密码
    database='comments',
    )

    cursor = db.cursor() #创建游标对象

    for i in range(100):
        
        res = requests.get('http://app.so.com/message/index?page='+str(i)+'&requestType=ajax&name=Outlook+Android_com.microsoft.office.outlook', headers=headers)
        # text = res.text.encode().decode("unicode_escape")
        if res.content == b'\n\n\n[]':
            break
        # soup = BeautifulSoup(text, 'html.parser')
        # print("Python 原始数据：",soup)

        json_str = json.loads(res.text) # 加载评论内容
        # print ("JSON 对象：", json_str)

        Comments = []

        for item in json_str:
            querysql = "select msgid from database_commentslist where msgid="+pymysql.converters.escape_string(str(item.get('msgid')))
            if(cursor.execute(querysql)==0):
            # print(querysql)
                sql = 'insert into database_commentslist(date,user,content,score,version,name, msgid) values(%s,%s,%s,%s,%s,%s,%s);'

                # print('------------------------')
                # print(item.get('score'))
                # print(item.get('version_name'))

                date = pymysql.converters.escape_string(item.get('create_time'))
                user = pymysql.converters.escape_string(item.get('username'))
                content = pymysql.converters.escape_string(item.get('content'))
                score = pymysql.converters.escape_string(str(item.get('score')))
                version = pymysql.converters.escape_string(str(item.get('version_name')))
                msgid = pymysql.converters.escape_string(str(item.get('msgid')))
                name = 'outlook'

                data = [date,user,content,score,version,name,msgid]
                # cursor.executemany(sql, data)
                cursor.execute(sql,data)     # 插入数据
            # print("sql",sql)
            # cds=cursor.fetchall()
            # print(res)

    print('Pages: ', i)
    cursor.close() 
    db.close()  #关闭数据库连接

 
def main():
    sample_job_every_600s()

if __name__ == '__main__':
    main()

