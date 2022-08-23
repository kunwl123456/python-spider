#模拟登录
import requests
from lxml import etree
#识别验证码
session=requests.Session()
url='https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4343.0 Safari/537.36'
}
page_text=session.get(url=url,headers=headers).text
tree=etree.HTML(page_text)
#解析验证码图片地址
img_src='https://so.gushiwen.cn'+tree.xpath('//*[@id="imgCode"]/@src')[0]
#将验证码存到本地
img_data=session.get(url=img_src,headers=headers).content
with open('./code.jpg','wb') as fp:
    fp.write(img_data)
code_text=transformImgCode('./code.jpg',1902)
print(code_text)
login_url='https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
data={
    '__VIEWSTATE': 'QGEuht8CM/gFytmYVUZI86PETVGk3UDhl5vSeiKIg/bDaQfIFSCY5Wwelqk+zoykvi7QNfCFM3Jeo/ESWqiXHqn9kc7TiqslGnGMHV6JtjPr04OXSpRLzUJhNZo=',
    '__VIEWSTATEGENERATOR': 'C93BE1AE',
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': 'youxiang@qq.com',
    'pwsd': '123456',
    'code': code_text,#动态变化
    'denglu': '登录',
}
#对登录页面发起请求
page_text_login=session.post(url=login_url,headers=headers,data=data).text
with open('./gushiwen.html','w',encoding='utf-8') as fp:
    fp.write(page_text_login)

