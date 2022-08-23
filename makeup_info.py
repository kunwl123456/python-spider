import requests
import json
url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4343.0 Safari/537.36'
}
id_list=[]
all_data_list=[]
for page in range(1,6):
    data = {
        'on':'true',
        'page':str(page),
        'pageSize':'15',
        'productName':'',
        'conditionType':'1',
        'applyname':'',
        'applysn':'',
}
    response=requests.post(url=url,headers=headers,data=data).json()
    for dic in response['list']:
       id_list.append(dic['ID'])
post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
for id in id_list:
    data = {'id': id}
    detail_json = requests.post(url=post_url, headers=headers, data=data).json()
    all_data_list.append(detail_json)

fp = open('allData.json', 'w', encoding='utf-8')
json.dump(all_data_list, fp=fp, ensure_ascii=False)
print('over!!!')  
————补充1：抓取一个产品信息（通过ID）
import requests
import json
url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
data={
    'id': '1246978d50094d849fc45defd4d93419',
}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4343.0 Safari/537.36'
}
response=requests.post(url=url,headers=headers,data=data)
page_text=response.json()
print(page_text)	
————补充2：抓取全部产品名字
import requests
import json
class Cfda:
    def __init__(self):
        self.url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    def getCfda(self,datas):
        self.html=requests.post(self.url,data=datas)
        #法一提取信息/批量 NO.1
        for m in range(15):
            self.data=self.html.json()['list'][m]['EPS_NAME']
            print(self.data)
            self.data2File(self.data)
        #法二函数式
        #map(lambda n:self.html.json(['list'][n]['ESP_NAME']))
    #定义写入保存文件
    def data2File(self,dat):
        with open ('.\cfda.txt','a',encoding='utf-8')as ff:
            ff.write(str(dat)+'\n')
cfda=Cfda()
for n in range(1,5):
    data={
        'on': 'true',
        'page': 'n',
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': '',
        'applysn':'', 
    }
cfda.getCfda(data)
