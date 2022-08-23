#余票检测
#从北京出发大概率不会是乱码开头，cookie残缺不影响使用，cookie内日期不影响使用
import requests
#session=requests.Session()
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4343.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie':'JSESSIONID=3FBB83C9AFAB3EF5D1052AA4F314C3A7; tk=ho_oPfAomA03WM_fK2f2YTw-Tznwd9MovrBKlhIpH0Edqk1k0; BIGipServerotn=351273482.24610.0000; BIGipServerpool_passport=199492106.50215.0000; RAIL_EXPIRATION=1612831908687; RAIL_DEVICEID=WNVRNfxup5o5bjzSdsMd0l72BhGjSilRLy9BvApyTxQoUiE-_SfMs42xzk7SWEV_K6wPylNMxRq1sJyndNISMepATrh3PCMl3Y-uIFims_Z8X3L_zKGGOm7f2vFUfzCwWQajbt8q4tMOwjc6CDFz10pTZfxDOzcn; route=6f50b51faa11b987e576cdb301e545c4; _jc_save_toDate=2021-02-05; _jc_save_wfdc_flag=dc; current_captcha_type=Z; uKey=926649402d6b95e884b574f58c1f9ff035bdbf9afc0254be3c9e77644ae15a25; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_toStation=%u91CD%u5E86%2CCQW; _jc_save_fromDate=2021-02-18',
    'Sec-Fetch-Site': 'same-origin',
    'Accept': '*/*',
}
city={
    '北京北':'VAP',
    '北京东':'BOP',
    '北京':'BJP',
    '北京南':'VNP',
    '北京西':'BXP',
    '广州南':'IJQ',
    '重庆北':'CUW',
    '重庆':'CQW',
    '重庆南':'CRW',
    '广州东':'GGQ',
    '上海':'SHH',
    '上海南':'SNH',
    '上海虹桥':'AOH',
}
t=input('entet a time:(yyyy-mm-dd):')
start=input('enter a start city:')
start=city[start]
end=input('enter a end city:')
end=city[end]
url='https://kyfw.12306.cn/otn/leftTicket/queryZ'
params={
    'leftTicketDTO.train_date': t,
    'leftTicketDTO.from_station': start,
    'leftTicketDTO.to_station': end,
    'purpose_codes': 'ADULT',
}
#返回的是json格式下data里的result的列表
json_data_list=requests.get(url=url,headers=headers,params=params).json()['data']['result']
#print(json_data_list)
#split为拆分函数
for s in json_data_list:
    print(s)
#json_data_list.split('')
项目十八#js解密
import execjs
import requests
#取当前电脑安装的js环境，没有的可以安装node.js
node = execjs.get()
# Params
method = 'GETCITYWEATHER'
city = '北京'
type = 'HOUR'
start_time = '2018-01-25 00:00:00'
end_time = '2018-01-25 23:00:00'
# Compile javascript打开要解密的js文件，先用compile编译js解密代码ctx
file = 'jsCode.js'
ctx = node.compile(open(file).read())
# Get params
js = 'getPostParamCode("{0}", "{1}", "{2}", "{3}", "{4}")'.format(method, city, type, start_time, end_time)
params = ctx.eval(js)
#发起post请求，获取页面源码数据
url = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'
response_text = requests.post(url, data={'d': params}).text
#对加密的响应数据进行解密，response__text是经过加密的邮箱地址，作为参数传给解密函数decodeData
js = 'decodeData("{0}")'.format(response_text)
#执行eval解密得到最终结果
decrypted_data = ctx.eval(js)
print(decrypted_data)
