# selenium是一个自动化的模块
# pip install selenium
# 谷歌浏览器驱动
# https://chromedriver.storage.googleapis.com/index.html
# 谷歌浏览器驱动与谷歌浏览器版本对应表
# https://blog.csdn.net/huilan_same/article/details/51896672
# mitmproxy防止selenium被屏蔽

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from lxml import etree
from time import sleep

chrome_option = Options()
# 无头浏览器（即不显示浏览器）
chrome_option.add_argument('--headless')
chrome_option.add_argument('--disable-gpu')
# 实例化一个浏览器对象
browser = webdriver.Chrome(options=chrome_option)
# 打开网页
browser.get('https://www.baidu.com/')

page_source = browser.page_source
baidu = etree.HTML(page_source)

li_list = baidu.xpath('//ul[@id="hotsearch-content-wrapper"]/li')

for li in li_list:
    news = li.xpath('.//span[@class="title-content-title"]/text()')
    print(news)

# 编写基于浏览器自动化的操作代码
# -发起请求: get(url)
# -标签定位: find系列的方法
# -标签交互: send_keys(xxx')
# -执行js程序: excute_script( jsCode')
# -前进，后退: back(),forward()
# -关闭浏览器:quit()
browser.quit()


# 实例化一个浏览器对象
browser = webdriver.Chrome()
# 打开网页
browser.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
browser.switch_to.frame('iframeResult')
div = browser.find_element('id', 'draggable')

action = ActionChains(browser)
action.click_and_hold(div)

for i in range(5):
    action.move_by_offset(40, 0).perform()
    sleep(0.4)

action.release()
browser.quit()