#获取ip字典
import requests
from lxml import etree
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4343.0 Safari/537.36'
}
url='http://ip.ipjldl.com/index.php/api/entry?method=proxyServer.generate_api_url&packid=1&fa=0&fetch_key=&groupid=0&qty=5&time=1&pro=&city=&port=1&format=html&ss=5&css=&dt=1&specialTxt=3&specialJson=&usertype=2'
page_text=requests.get(url=url,headers=headers).text
tree=etree.HTML(page_text)
proxy_list=tree.xpath('//body//text()')
http_proxy=[]
for proxy in proxy_list:
    dic={
        'https':proxy
    }
    proxy_list.append(dic)
#用的话放在requests.get（url=new_url,headers=headers,proxies=randdom.choice(http_proxy)）
