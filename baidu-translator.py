import requests
import json

if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    url = "https://fanyi.baidu.com/sug"
    data = {
        'kw': 'dog'
    }
    response = requests.get(url=url, params=data, headers=headers)
    res = response.json()
    file_name = data['kw']+'.json'
    fp = open(file_name, 'w', encoding='utf-8')
    json.dump(res, fp=fp, ensure_ascii=False)
    print('爬取结束')
