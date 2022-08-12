## 后端爬虫
### `360_scrapy.py` ：jinghan 写的360爬虫

### `huawei`文件夹 ： libo 写的华为爬虫
### 以上两个是requests库实现静态网页爬取

### `diandian.py`：点点数据网爬虫封装，使用selenium实现
### `all.py`：oppo，vivo，xiaomi，应用宝的点点数据爬虫

---

### `django_app` ： django框架
### `database` ：django的app，用于数据库操作
## 前端
### `front_to_end`：zongyang 写的网站


---

### `main` 分支在Windows下运行，若是Linux服务器，爬虫时需要在webdriver加入以下option字段。（可查看`centos7.9` 分支）

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
### `centos7.9`分支在centos7.9系统下运行

---

### `requirements`：环境运行需要的库