# 爬取搜狗首页

import requests

if __name__ == "__main__":
    # 目标url
    url = 'https://www.sogou.com/'
    # 发送请求
    response = requests.get(url=url)
    # 获取响应数据
    page_text = response.text
    # 持久化存储
    with open('./sogou.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取结束')
