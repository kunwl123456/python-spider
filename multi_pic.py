#爬取多页的
#定义一个通用url模板
import requests
dirName='GirlsLibs'
if not os.path.exists(dirName):
    os.mkdir(dirName)
url='http://pic.netbian.com/4kmeinv/index_%d.html'
#for循环第一页到第五页
for page in range(1,6):
    if page ==1:
        new_url='http://pic.netbian.com/4kmeinv/'
    else:
        new_url=format(url%page)
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4343.0 Safari/537.36'
    }
    response=requests.get(url=new_url,headers=headers)
    response.encoding='gbk'
    page_text=response.text
    #图片数据和图片名称
    tree=etree.HTML(page_text)
    li_list=tree.xpath('//div[@class="slist"]//li')
    for li in li_list:
        #进行局部数据解析,在局部数据解析中./表示当前的局部数据
        title=li.xpath('./a/img/@alt')[0]+'.jpg'
        img_src='http://pic.netbian.com'+li.xpath('./a/img/@src')[0]
        #print(title,img_src)
        img_data=requests.get(url=img_src,headers=headers).content
        imgPath=dirName+'/'+title
        with open (imgPath,'wb')as fp:
            fp.write(img_data)
        print(title,'保存成功！！！')
