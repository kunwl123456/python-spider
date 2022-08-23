import requests
headers={
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4343.0 Safari/537.36'
}
#创建好了session对象
#假设第一访问主页就发送了cookies请求
session=requests.Session()
main_url='https://xueqiu.com/'
#捕获且存储cookies
session.get(url=main_url,headers=headers)
url='https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=164856&size=15'
#携带cookies发起的请求
page_text=session.get(url=url,headers=headers).json()
page_text
