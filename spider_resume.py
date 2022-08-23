import requests
from lxml import etree
import os
#给要存储的文件命名resume
dirName ='./resumeLibs'
#不存在文件就创建
if not os.path.exists(dirName):
    os.mkdir(dirName)
#加UA伪装
headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4343.0 Safari/537.36',
}
#首页url
url ='http://sc.chinaz.com/jianli/free_%d.html'
#爬前两页
for page in range(1,2):
    if page == 1:
        new_url='https://sc.chinaz.com/jianli/free.html'
    else:
        new_url=format(url%page)
    #获取页面源码数据
    page_text_1= requests.get(url=new_url,headers=headers).text
    #设置编码
    #page_text.encoding ='utf-8'
    #page_text=page_text.text
    tree = etree.HTML(page_text_1)
    a_list = tree.xpath('//div[@id="container"]/div/p/a')
    for a in a_list:
        a_src='http:'+a.xpath('./@href')[0]
        #输出要爬虫的文件名字为a_title
        a_title=a.xpath('./text()')[0]
        a_title=a_title.encode('iso-8859-1').decode('utf-8')
        #爬取下载页面
        page_text=requests.get(url=a_src,headers=headers)
        page_text.encoding ='utf-8'
        page_text=page_text.text
        tree=etree.HTML(page_text)
        #dl_src为下载链接
        dl_src=tree.xpath('//div[@id="down"]/div[2]/ul/li[8]/a/@href')[0]
        resume_data=requests.get(url=dl_src,headers=headers).content
       # print(resume_data)
        #文件路径为resume_path
        resume_name=a_title
        resume_path=dirName + '/' + resume_name + '.rar'
        with open(resume_path,'wb') as fp:
            fp.write(resume_data)
            print(resume_name,'下载成功!')
