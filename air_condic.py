#爬取空气质量历史数据查询的城市
import requests
url='https://www.aqistudy.cn/historydata/'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4343.0 Safari/537.36'
}
page_text=requests.get(url=url,headers=headers).text
tree=etree.HTML(page_text)
#爬热门城市
hot_cities=tree.xpath('//div[@class="bottom"]/ul/li/a/text()')
#爬二线城市
all_cities=tree.xpath('//div[@class="bottom"]/ul/div[2]/li/a/text()')
#爬全部城市
tree.xpath('//div[@class="bottom"]/ul/li/a/text()|//div[@class="bottom"]/ul/div[2]/li/a/text()')
