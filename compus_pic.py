import requests
import re
import urllib
import os
#创建文件夹dirName
dirName='ImgLibs'
#若文件夹ImgLibs不存在，则创建make一个ImgLibs文件夹
if not os.path.exists(dirName):
    os.mkdir(dirName)
#1捕捉当前页面源码数据
url='http://www.521609.com/tuku/shz/'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4343.0 Safari/537.36'
}
page_text=requests.get(url=url,headers=headers).text
#2从当前获取的页面源码数据中解析出图片地址,(.*?)为图片地址
ex='<li>.*? <img src="(.*?)" alt=.*?</li>'
#re.s处理换行
img_src_list=re.findall(ex,page_text,re.S)
for src in img_src_list:
    src = 'http://www.521609.com'+src
    #src.split['/']为根据/分组，[-1]表示拿到最后一个结束,
    imgPath = dirName+'/'+src.split('/')[-1]
    urllib.request.urlretrieve(src,imgPath)
    print(imgPath,'下载成功！！！')
