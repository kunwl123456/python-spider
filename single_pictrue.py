import requests
import urllib
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4343.0 Safari/537.36'
}
img_url='https://pics0.baidu.com/feed/738b4710b912c8fc1184111ed2ef6542d48821e6.jpeg?token=16e99d15cb2ef84747689a6dbebbf2ae&s=6843961A10F84C296AC389CC030070BB'
response=requests.get(url=img_url,headers=headers)
img_data=response.content
with open ('i.jpg','wb')as fp:
    fp.write(img_data)
————补充:基于urllib爬取图片
import urllib
import requests
img_url='https://pics4.baidu.com/feed/e61190ef76c6a7ef335198d46f005756f1de66cb.jpeg?token=d8391cac8b7cb8c79188fd602eb8e5ef&s=22A021A84E1207FD96A154880300E0F2'
urllib.request.urlretrieve(img_url,'./2.jpg')
