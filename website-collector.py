import requests

if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    url = "https://www.sogou.com/web"
    kw = input('enter a keyword:')
    query = {
        'query': kw
    }

    response = requests.get(url=url, params=query, headers=headers)
    page_text = response.text
    file_name = kw + '.html'

    with open(file_name, 'w', encoding="utf-8") as fp:
        fp.write(page_text)

    print(file_name, '保存成功！！！')