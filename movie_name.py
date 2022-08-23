import requests
def get_movies():
    headers={
        'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
        'Host':'movie.douban.com'
    }
    movie_list=[]
    for i in range(0,10):
        link='https://movie.douban.com/top250?start='+str(i*25)+'&filter='
        r=requests.get(link,headers=headers,timeout=10)
        print(str(i+1),"页面响应码：",r.status_code)
        soup=BeautifulSoup(r.text,"lxml")
        div_list=soup.find_all('div',class_='hd')
        for each in div_list:
            #print(str(i+1),"页面响应码：",r.status_code)
            movie=each.a.span.text.strip()
            movie_list.append(movie)
    return movie_list
movies=get_movies()
print(movies)
————补充：捕动态加载数据的电影数据
import requests
import json
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4343.0 Safari/537.36'
}
url='https://movie.douban.com/j/search_subjects'
params={
    'type': 'tv',
    'tag': '综艺',
    'sort': 'recommend',
    'page_limit': '10',
    'page_start': '0',
}
response = requests.get(url=url,params=params,headers=headers)
#.json（）将获取的字符串形式的json数据序列化成字典或列表对象
page_text=response.json()
for movie in page_text["subjects"]:
    name = movie['title']
    rate = movie['rate']
    print(name,rate)
