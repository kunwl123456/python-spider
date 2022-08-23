from selenium import webdriver
from time import sleep
from lxml import etree
url='http://scxk.nmpa.gov.cn:81/xk/'
#1,基于浏览器的驱动程序实例化一个浏览器对象
bro=webdriver.Chrome(executable_path='chromedriver')
bro.get(url)
#page_text_list存放每一页的页面源码数据
page_text_list=[]
#等一秒
sleep(1)
#捕获到页面源码数据(page_souce捕获到所有数据，返回的是当前页面全部加载后的数据)
page_text=bro.page_source
page_text_list.append(page_text)
sleep(1)
for i in range(2):
#找到下一页的按钮，点击下一页
    next_page=bro.find_element_by_xpath('//*[@id="pageIto_next"]')
    next_page.click()
    sleep(1)
    #获得下一页的页面源码数据,并存到列表page_text_list中
    page_text_list.append(bro.page_source)
#将列表里面的每一页页面源码数据都解析
for page_text in page_text_list:
    tree=etree.HTML(page_text)
    li_list=tree.xpath('//*[@id="gzlist"]/li')
    for li in li_list:
        name=li.xpath('./dl/@title')[0]
        print(name)
sleep(2)
#关闭浏览器
bro.quit()
_______补充：抓包调剂信息
from selenium import webdriver
from time import sleep
from lxml import etree
url='http://muchong.com/bbs/kaoyan.php?page=4&page=1'
#1,基于浏览器的驱动程序实例化一个浏览器对象
bro=webdriver.Chrome(executable_path='chromedriver')
bro.get(url)
#page_text_list存放每一页的页面源码数据
page_text_list=[]
#等一秒
sleep(1)
#捕获到页面源码数据(page_souce捕获到所有数据，返回的是当前页面全部加载后的数据)
page_text=bro.page_source
page_text_list.append(page_text)
sleep(1)
#由于是range(2)，故为抓前三页
for i in range(2):
#找到下一页的按钮，点击下一页
    next_page=bro.find_element_by_xpath('//tr/td[9]/a[@href]')
    next_page.click()
    sleep(1)
    #获得下一页的页面源码数据,并存到列表page_text_list中
    page_text_list.append(bro.page_source)
#将列表里面的每一页页面源码数据都解析
for page_text in page_text_list:
    tree=etree.HTML(page_text)
    li_list=tree.xpath('//tr')
    #print(li_list)
    for li in li_list:
        name=li.xpath('./td[2]/text()')
        print(name)
sleep(2)
#关闭浏览器
#print(page_text_list)
bro.quit()
