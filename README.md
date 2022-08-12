### 360_scrapy.py ：jinghan 写的360爬虫代码
### huawei文件夹 ： libo 写的华为爬虫代码
### front_to_end:zongyang 写的网站
### django_app ： django框架
### database ：django的app，用于数据库操作
### requirements：环境设置
### main分支是Windows下运行，若是Linux服务器系统需要在webdriver加入option
```python
from selenium.webdriver.chrome.options import Options

ch_options = webdriver.ChromeOptions()
#为Chrome配置无头模式
ch_options.add_argument("--headless")  
ch_options.add_argument('--no-sandbox')
ch_options.add_argument('--disable-gpu')
ch_options.add_argument('--disable-dev-shm-usage')
# 在启动浏览器时加入配置

driver = webdriver.Chrome(options=ch_options)
```
