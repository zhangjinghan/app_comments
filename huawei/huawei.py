from pyparsing import col
import requests
import pandas as pd
import pymysql
from sqlalchemy import create_engine, true

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
# C100148961 edge
# office C10888510
# outlook C100502955

# 连接数据库
db = pymysql.connect(

host="127.0.0.1", 
port=3306,
user='root',    #在这里输入用户名
password='root',     #在这里输入密码
database='comments',
)

mysql_setting = {
        'host': '127.0.0.1',  # 数据库地址，本机 ip 地址 127.0.0.1
        'port': 3306,  # 端口
        'user': 'root',  # 数据库用户名
        'passwd': 'root',  # 数据库密码
        'db':'comments',
        'charset': 'utf8'
}


cursor = db.cursor() #创建游标对象

for page in range(1, 10):

    params = {
        'method': 'internal.user.commenList3',
        'serviceType': '20',
        'reqPageNum': page,
        'maxResults': '25',
        'appid': 'C100148961',
        'version': '10.0.0',
        'zone': '',
        'locale': 'zh',
    }

    # 请求的链接 ，添加参数和请求头
    #  使用的 requests 库的 get 方法
    response = requests.get('https://web-drcn.hispace.dbankcloud.cn/uowap/index', params=params, headers=headers)
    import json

    # 将传递的数据转换为 json 文件，可以提取具体的评论内容
    con = json.loads(response.text)
    # 提取存储评论内容的列表
    data = con['list']


    for i in data:
        print(i)
        nickname = i['accountName']  # 昵称
        comment = i['commentInfo']  # 评价内容
        operTime = i['operTime']  # 评价时间
        phone = i['phone']  # 手机型号
        rating = i['rating']  # 评分


        sql = 'insert into database_huaweicomments(nickname, comment, operTime, phone, rating) values(%s,%s,%s,%s,%s);'

        nickname1 = pymysql.converters.escape_string(str(i.get('accountName')))
        comment1 = pymysql.converters.escape_string(str(i.get('commentInfo')))
        operTime1 = pymysql.converters.escape_string(str(i.get('operTime')))
        phone1 = pymysql.converters.escape_string(str(i.get('phone')))
        rating1 = pymysql.converters.escape_string(str(i.get('rating')))

        huaweidata = [nickname1, comment1, operTime1, phone1, rating1]
        # print(huaweidata)
        # cursor.execute(sql,huaweidata)     #执行sql语句

        # print([nickname, comment, operTime, phone, rating])
        data_all.append(huaweidata)

df = pd.DataFrame(data_all, columns=['nickname', 'comment', 'operTime', 'phone', 'rating'])

df.to_csv('./edge.csv', encoding="utf_8")
 
# 表名
# 如果不存在表，则自动创建
table_name = 'database_huaweicomments'
path = './edge.csv'
comments_data = pd.read_csv(path,encoding='utf-8')
engine = create_engine("mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}".format(**mysql_setting), max_overflow=5)
comments_data.to_sql(table_name,engine,index=true,if_exists='replace',)
print('导入成功...')

print(comments_data.head(5))