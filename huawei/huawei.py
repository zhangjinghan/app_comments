
from pyparsing import col
import requests
import pandas as pd
import pymysql
from sqlalchemy import create_engine, true
import json
# 请求头部 计算机网络知识
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'Connection': 'keep-alive',
    'Origin': 'https://appgallery.huawei.com',
    'Referer': 'https://appgallery.huawei.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

# 存储所有数据的列表
data_all = []
# 通过在浏览器抓包 获取评论加载的动态链接 通过传递数据来修改数据请求页数
# 修改 appid 可以抓取不同的 app 的内容
#  注意也要修改下面的保存表格的名字
# edge C100148961 
# office C10888510
# outlook C100502955
# teams C100427405
appdict={
    'C100148961':'edge',
    'C10888510':'office',
    'C100502955':'outlook',
    'C100427405':'teams',
    'C100170015':'onedrive',
    'C10586094':'Word',
    'C10586102':'Excel',
    'C10586107':'PowerPoint',
    'C103244819':'OneNote',
    'C100488045':'Microsoft Launcher',
}

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

for k,v in appdict.items():
    for page in range(1, 10):
        params = {
            'method': 'internal.user.commenList3',
            'serviceType': '20',
            'reqPageNum': page,
            'maxResults': '25',
            'appid': k,
            'version': '10.0.0',
            'zone': '',
            'locale': 'zh',
        }

        # 请求的链接 ，添加参数和请求头
        #  使用的 requests 库的 get 方法
        response = requests.get('https://web-drcn.hispace.dbankcloud.cn/uowap/index', params=params, headers=headers)
        # 将传递的数据转换为 json 文件，可以提取具体的评论内容
        con = json.loads(response.text)
        # print(con)
        # 提取存储评论内容的列表
        if 'list' in con:
            data = con.get('list')
            for i in data:
                print(i)
                # nickname = i['accountName']  # 昵称
                # comment = i['commentInfo']  # 评价内容
                # operTime = i['operTime']  # 评价时间
                # phone = i['phone']  # 手机型号
                # rating = i['rating']  # 评分

                sql = 'insert into database_comments_huawei(nickname, comment, operTime, phone, rating, appname) values(%s,%s,%s,%s,%s,%s);'

                # msgid = pymysql.converters.escape_string(str(i.get('commentId')))
                nickname1 = pymysql.converters.escape_string(str(i.get('accountName')))
                # print(nickname1)
                comment1 = pymysql.converters.escape_string(str(i.get('commentInfo')))
                # print(comment1)
                operTime1 = pymysql.converters.escape_string(str(i.get('operTime')))
                phone1 = pymysql.converters.escape_string(str(i.get('phone')))
                rating1 = pymysql.converters.escape_string(str(i.get('rating')))
                appname1 = pymysql.converters.escape_string(str(v))
                # data = ['msgid','nickname', 'comment', 'operTime', 'phone', 'rating'] 

                huaweidata = [nickname1, comment1, operTime1, phone1, rating1,appname1]
                print(huaweidata)
                cursor.execute(sql,huaweidata)     # 插入数据
                db.commit() # 提交请求

                data_all.append(huaweidata)
cursor.close() 
db.close()  #关闭数据库连接

