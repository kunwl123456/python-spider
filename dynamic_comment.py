import requests
link="https://api-zero.livere.com/v1/comments/list?callback=jQuery11240224188209204927_1611757460252&limit=10&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&code=&_=1611757460254"
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'
}
r=requests.get(link,headers=headers)
import json
json_string=r.text
#仅仅提取字符串中符合json格式的部分
json_string=json_string[json_string.find('{'):-2]
#json.loads 可以把字符串格式的响应体数据转化为 json 数据
json_data=json.loads(json_string)
#利用 json 数据的结构，我们可以提取到评论的列表comment_list
coment_list=json_data['results']['parents'] 
for eachone in coment_list:
    message=eachone['content']
print(message)


————————补充项目二
#爬取各个页面的评论
import requests
import json
def single_page_comment(link):
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    r = requests.get(link, headers= headers)
    # 获取 json 的 string
json_string = r.text
#仅仅提取字符串中符合json格式的部分
json_string = json_string[json_string.find('{'):-2]
#json.loads 可以把字符串格式的响应体数据转化为 json 数据	
    json_data = json.loads(json_string)
    comment_list = json_data['results']['parents']
    for eachone in comment_list:
        message = eachone['content']
        print (message)
for page in range(1,4):
    link1 = "https://api-zero.livere.com/v1/comments/list?callback=jQuery112403473268296510956_1531502963311&limit=10&offset="
    link2 = "&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1531502963316"
    page_str = str(page)
    link = link1 + page_str + link2
    print (link)
single_page_comment(link)

