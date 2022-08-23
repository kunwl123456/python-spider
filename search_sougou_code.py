url='https://www.sogou.com/'
#对网页发起requests的请求
reponse=requests.get(url=url)
#获取.text格式的文件
page_text=response.text
#保存网页名为sougou.html格式为utf-8的文件
with open('./sougou.html','w',encoding='utf-8') as fp:
fp.write(page_text)
——————补充：抓取关键字搜索结果页面
import requests
#设立user-agent反UA检测
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4343.0 Safari/537.36'
}
keyword = input ('enter a key word:')
#实现参数动态化
params={
    'query':keyword
}
url='https://www.sogou.com/web'
#对网页发起requests的请求
response=requests.get(url=url,params=params,headers=headers)
#获取.text格式的文件
page_text=response.text
#encoding返回的是响应数据的原始编码格式，如果给其赋值则改变响应数据的编码格式
response.encoding = 'utf-8'
fileName=keyword+'.html'
#保存网页名为sougou.html格式为utf-8的文件
with open(fileName,'w',encoding='utf-8') as fp:
    fp.write(page_text)
print(fileName,"爬取完毕!!!")
