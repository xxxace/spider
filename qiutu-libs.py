import requests
import re
import os

if __name__ == "__main__":
    url = ""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    if not os.path.exists('./qiutuLibs'):
        os.mkdir("./quituLibs")

    page_text = requests(url=url, headers=headers).text

    pattern = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    img_src_list = re.findall(pattern, page_text, re.S)
    for src in img_src_list:
        src = "https:"+src
        img_data = requests.get(url=src, headers=headers).content
        img_name = src.split('/')[-1]
        img_path = "./qiutuLibs/"+img_name
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name, '下载成功！')
