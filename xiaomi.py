
import imp
from xml.etree.ElementTree import Comment
import requests
import json
import time
from timeloop import Timeloop
from  datetime import timedelta
from bs4 import BeautifulSoup
import pymysql

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host':'api.diandian.com',
    'Origin':'https://appold.diandian.com',
    'Referer': 'https://appold.diandian.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Cookie':'Qs_lvt_404253=1659626539; _gcl_au=1.1.850170264.1659626600; Qs_pv_404253=3421427176112213000,1257341401756732700,4309564494115419000,3444972530415304700,3916888100567570000'

    
}

testjson = {"code":0,"msg":"success","data":{"list":[{"id":"k1cpu6rdd293rxbw","rating":5,"review_text":"\u6700\u597d\u7684\u6d4f\u89c8\u5668\u6ca1\u6709\u4e4b\u4e00","review_time":1659505868,"status_id":1,"version":"102.0.1245.44","likes":0,"replies":0,"user":{"id":"1405692551","name":"14***51","avatar":""},"app_id":"516732","levle_comment":{}},{"id":"xqcpuvzroz5mroil","rating":5,"review_text":"\u633a\u8212\u670d\u7684\u754c\u9762","review_time":1659459113,"status_id":1,"version":"103.0.1264.71","likes":1,"replies":0,"user":{"id":"2577814700","name":"25***00","avatar":""},"app_id":"516732","levle_comment":{}},{"id":"9zcdulx37vvg9dhj","rating":5,"review_text":"\u8d44\u8baf\u4e00\u5173\uff0c\u4e16\u754c\u90fd\u6e05\u51c0\u4e86","review_time":1659442686,"status_id":1,"version":"103.0.1264.71","likes":0,"replies":0,"user":{"id":"2576832045","name":"25***45","avatar":""},"app_id":"516732","levle_comment":{}},{"id":"zqc9u51pgdqkwghv","rating":5,"review_text":"\u597d\u5c31\u5b8c\u4e8b","review_time":1659436133,"status_id":1,"version":"103.0.1264.62","likes":0,"replies":0,"user":{"id":"2275877558","name":"22***58","avatar":""},"app_id":"516732","levle_comment":{}},{"id":"vwcmurp528d79oug","rating":0,"review_text":"\u597d\u591a\u90fd\u6253\u5f00\u4e0d\u4e86\ud83d\ude14","review_time":1659425775,"status_id":1,"version":"","likes":0,"replies":0,"user":{"id":"2189581736","name":"21***36","avatar":""},"app_id":"516732","levle_comment":{}},{"id":"pkcgu7prw6olk5c7","rating":5,"review_text":"\u8d85\u7ea7\u597d\u7528\u597d\u561b\uff0c\u5bb6\u4eba\u4eec\u90fd\u7ed9\u6211\u51b2","review_time":1659424979,"status_id":1,"version":"103.0.1264.71","likes":2,"replies":0,"user":{"id":"2540854646","name":"25***46","avatar":""},"app_id":"516732","levle_comment":{}},{"id":"glcvujd52d1moef6","rating":2,"review_text":"\u4f60\u6700\u8fd1\u662f\u641c\u7d22\u5f15\u64ce\u662f\u6709\u4ec0\u4e48\u95ee\u9898\u5417\uff0c\u52a8\u4e0d\u52a8\u5c31\u5c31\u65e0\u6cd5\u8bbf\u95ee\uff0c\u4ec0\u4e48\u4e1c\u897f\u90fd\u8fd9\u6837","review_time":1659411482,"status_id":1,"version":"103.0.1264.71","likes":2,"replies":1,"user":{"id":"2477804045","name":"24***45","avatar":""},"app_id":"516732","levle_comment":{"list":[{"comment_id":"23c2i2z8mpwlzdu1","version":"","review_text":"\u90a3\u5f97\u770b\u4f60\u641c\u7684\u662f\u4ec0\u4e48\u4e86","review_time":1659597116,"likes":0,"user_type":0,"user":{}}],"count":1}},{"id":"k1cpu6rd3xwzrqaw","rating":5,"review_text":"\u5e72\u5e72\u51c0\u51c0\uff0c\u53ef\u4ee5\u8bbe\u7f6e\u6210\u6ca1\u6709\u63a8\u9001\uff0c\u771f\u597d","review_time":1659369193,"status_id":1,"version":"103.0.1264.71","likes":0,"replies":0,"user":{"id":"178912628","name":"17***28","avatar":""},"app_id":"516732","levle_comment":{}},{"id":"oxcvux0qrkg28xi9","rating":5,"review_text":"\u6211\u60f3\u770b\u7684\u57fa\u672c\u627e\u5f97\u5230","review_time":1659364390,"status_id":1,"version":"103.0.1264.71","likes":0,"replies":0,"user":{"id":"2545632368","name":"25***68","avatar":""},"app_id":"516732","levle_comment":{}},{"id":"jqcmu16365z9xqhp","rating":4,"review_text":"\u7b80\u6d01\uff0c\u597d\u7528\uff0c\u5c31\u662f\u5bf9\u4f4e\u914d\u624b\u673a\u4e0d\u53cb\u597d\uff0c\u603b\u4f53\u6765\u8bf4\u8fd8\u662f\u4e0d\u9519\u7684","review_time":1659362851,"status_id":1,"version":"103.0.1264.71","likes":1,"replies":0,"user":{"id":"2499437215","name":"24***15","avatar":""},"app_id":"516732","levle_comment":{}}]}}
# text = json.loads(testjson)
# print(testjson["data"]['list'])
for item in testjson["data"]['list']:
    # print(item.get('id'))
    print(item.get('rating'))
    print(item.get('review_text').encode('utf-8', 'replace').decode())
    print(item.get('review_time'))
    print(item.get('version'))
    print(item.get('app_id'))
    print(item.get('user')['name'])


appname = {
    'outlook':'Outlook+Android_com.microsoft.office.outlook',
    'office':'Office+Mobile+for+Office+365+Android_com.microsoft.office.officehub',
    'edge':'微软浏览器+Android_com.microsoft.emmx'
}

# 定时模块
tl = Timeloop()
@tl.job(interval=timedelta(seconds=600))
def sample_job_every_600s():
    # # 连接数据库
    # db = pymysql.connect(
    
    # host="127.0.0.1", 
    # port=3306,
    # user='root',    #在这里输入用户名
    # password='root',     #在这里输入密码
    # database='comments',
    # charset='utf8mb4'
    # )

    # cursor = db.cursor() #创建游标对象
    # for k,v in appname.items():
    # for i in range(100):
        
        res = requests.get('https://api.diandian.com/pc/app/v1/comment?model=&id=6njqcmu6xj0rip4&country_id=75&topic_num=0&type=0&rating=0&sort=1&word=&version=&language_id=3&page=7&page_size=10&k=V1JfVVpaUkEUAV5RVlZbWlJBFAlRUFZUW11QQU9aFgECEV0SCUdTWRdWWFNeQkVRCAFXUlxTXlhRQRAYQURGAA9CRVEIHxFTQAcEBw4ST0Q=', headers=headers)
        # text = res.text.encode().decode("unicode_escape")
        # if res.content == b'\n\n\n[]':
        #     break
        # soup = BeautifulSoup(res.text, 'lxml')
        # print("Python 原始数据：",res.text)
        # print("soup",soup.select('.content'))

        # json_str = json.loads(res.text) # 加载评论内容
        # print ("JSON 对象：", json_str)

        Comments = []

        # for item in json_str:
            # querysql = "select msgid from database_comments_360 where msgid="+pymysql.converters.escape_string(str(item.get('msgid')))
            # if(cursor.execute(querysql)==0):
            # print(querysql)
            # sql = 'insert into database_comments_360(date,user,content,score,version,name, msgid) values(%s,%s,%s,%s,%s,%s,%s);'

            # print('------------------------')
            # print(item)
            # print(item.get('version_name'))

            # date = pymysql.converters.escape_string(item.get('create_time'))
            # user = pymysql.converters.escape_string(item.get('username'))
            # content = pymysql.converters.escape_string(item.get('content'))
            # score = pymysql.converters.escape_string(str(item.get('score')))
            # version = pymysql.converters.escape_string(str(item.get('version_name')))
            # msgid = pymysql.converters.escape_string(str(item.get('msgid')))
            # name = 'outlook'

            # data = [date,user,content,score,version,name,msgid]
            # # cursor.executemany(sql, data)
            # cursor.execute(sql,data)     # 插入数据
            # db.commit()
            # print("sql",sql)
            # cds=cursor.fetchall()
            # print(res)

    # print('爬取'+str(k)+'应用评论'+str(i)+'页')
    # cursor.close() 
    # db.close()  #关闭数据库连接

 
def main():
    sample_job_every_600s()

if __name__ == '__main__':
    main()

