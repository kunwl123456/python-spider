from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
from lxml import etree
url='https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
bro=webdriver.Chrome(executable_path='chromedriver')
bro.get(url)
sleep(1)
#定位标签
#若通过find定位进行在iframe下面的标签，则会定位失败
bro.switch_to.frame('iframeResult')
div_tag=bro.find_element_by_xpath('//*[@id="draggable"]')
print(div_tag)
#对div_tag进行滑动
#对指定浏览器生成动作链
action=ActionChains(bro)
#对div_tag点击和长按
action.click_and_hold(div_tag)
for i in range(6):
    #perform让动作链执行
    action.move_by_offset(10,15).perform()
    sleep(0.5)
action.release()
bro.quit()
项目十七#selenium的无可视化操作(给网页截图)
from selenium import webdriver
from time import sleep
import time
#实现无可视化界面
from selenium.webdriver.chrome.options import Options
#实现规避检测
#from selenium.webdriver import ChromeOptions
#实现无可视化界面的操作
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
#创建浏览器对象
browser= webdriver.Chrome(executable_path='./chromedriver',chrome_options=chrome_options)
#上网
url='http://www.baidu.com/'
browser.get(url)
time.sleep(3)
#截图
browser.save_screenshot('baidu.png')
print(browser.page_source)
browser.quit()
