import requests
fp=open('./sanguo.txt','w',encoding='utf-8')
main_url='https://www.shicimingju.com/book/sanguoyanyi.html'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4343.0 Safari/537.36'
}
response=requests.get(url=main_url,headers=headers)
response.encoding="utf-8"
page_text=response.text
#数据解析：章节标题，详情页url，章节内容
soup=BeautifulSoup(page_text,'lxml')
#定位到所有符合要求的a标签
a_list = soup.select('.book-mulu>ul>li>a')
for a in a_list:
    #获取标题在li内的字符串
    title = a.string
    #获取文章的url
    detail_url='https://www.shicimingju.com'+a['href']
    #对详情页发起请求解析出章节内容
    responses=requests.get(url=detail_url,headers=headers)
    responses.encoding="utf-8"
    page_text_detail=responses.text
    soup=BeautifulSoup(page_text_detail,'lxml')
    div_tag=soup.find('div',class_='chapter_content')
    #div_tag.encoding="utf-8"
    content=div_tag.text
    #写入文件夹
    fp.write(title+':'+content+'\n')
    print(title,'保存成功！！！')
fp.close()
