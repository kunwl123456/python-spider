class Chaojiying_Client(object):
    def __init__(self, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }
    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()
    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()
from selenium import webdriver
import time
import requests
from lxml import etree
from urllib import request
#导入动作链
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
#1，用selenium打开登录界面
bro = webdriver.Chrome(executable_path='./chromedriver')
bro.get('https://kyfw.12306.cn/otn/resources/login.html')
time.sleep(1)
next_page=bro.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a')
next_page.click()
#2，对当前selenium打开的界面进行截图,save_screenshot将当前页面截图并保存
bro.save_screenshot('aa.png')
#定位照片标签
code_img_ele=bro.find_element_by_xpath('//*[@id="J-loginImg"]')
location=code_img_ele.location#返回验证码图片的x,y坐标
print('location:',location)
size=code_img_ele.size#返回验证码图片标签对应的长和宽
print('size:',size)
##确认验证码的左上角和右下角的坐标
rangle = (
int(location['x']), int(location['y']), int(location['x'] + size['width']), int(location['y'] + size['height']))
#3，使用超级鹰识别验证码图片，实例化img对象
i = Image.open('./aa.png')
code_img_name = './code.png'
#crop根据指定区域进行图片裁剪
frame = i.crop(rangle)
#frame.save对截图的图片进行保存，保存图片名字为code.png
frame.save(code_img_name)
#4,将验证码图片提交给超级鹰识别
if __name__ == "__main__":
    chaojiying =Chaojiying_Client('超级鹰账号', '超级鹰密码', '超级鹰付费编号')
    im = open('code.png', 'rb').read()
    print chaojiying.PostPic(im, 9004)['pic_str']
    result=chaojiying.PostPic(im, 9004)['pic_str']
#返回来的验证码地址信息放到result中
    all_list=[]#存储被点击点的坐标
    if '|' in result:
        list_1 = result.split('|')
        count_1 = len(list_1)
        for i in range(count_1):
            xy_list = []
            x = int(list_1[i].split(',')[0])
            y = int(list_1[i].split(',')[1])
            xy_list.append(x)
            xy_list.append(y)
            all_list.append(xy_list)
    else:
        x = int(result.split(',')[0])
        y = int(result.split(',')[1])
        xy_list = []
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)
    print(all_list)
#遍历列表，使用动作链对每一个列表元素对应的x,y指定的位置进行点击操作
    for l in all_list:
        x = l[0]
        y = l[1]
        ActionChains(bro).move_to_element_with_offset(code_img_ele, x, y).click().perform()
        time.sleep(0.5)
#输入用户名和密码
    bro.find_element_by_id('username').send_keys('youxiang@qq.com')
    time.sleep(2)
    bro.find_element_by_id('password').send_keys('password')
    time.sleep(2)
    bro.find_element_by_id('loginSub').click()
    time.sleep(30)
    bro.quit()
