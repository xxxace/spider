from lxml import etree
from multiprocessing.dummy import Pool
import requests
import re
import random
from datetime import datetime
from http import cookies
from urllib.parse import urlparse


def get_real_url(url, video_id):
    return re.sub(r'(?<=/)\d+(?=-)', 'cont-'+video_id, url)


if __name__ == "__main__":
    print('任务开始：')
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    }

    c = {
        'id': "9707bc8d5f6bba210e7218b8496f076a",
        'dm': ["pearvideo.com"],
        'js': "tongji.baidu.com/hm-web/js/",
        'vdur': 1800000,
        'age': 31536000000,
    }

    m = {
        'B': round(datetime.now().timestamp() / 1E3)
    }

    cookie = cookies.SimpleCookie()
    cookie['Hm_lvt_'+c['id']] = "1688613004"
    cookie['Hm_lvt_'+c['id']]['max-age'] = c['age']
    cookie['Hm_lpvt_'+c['id']] = "1688623822"

    host = "https://www.pearvideo.com/"
    category_url = host+"/category_5"
    session = requests.session()
    session.cookies.update(cookie)
    page_res = session.get(url=category_url, headers=headers)

    page = etree.HTML(page_res.text)
    li_list = page.xpath('//ul[@id="listvideoListUl"]/li')
    video_url_list = []

    get_video_url = 'https://www.pearvideo.com/videoStatus.jsp'
    for li in li_list:
        detail_url = host+li.xpath('./div/a/@href')[0]
        name = li.xpath('./div/a/div[2]/text()')[0]+'.mp4'
        cont_id = detail_url.split('_')[-1]
        params = {
            "contId": cont_id,
            "mrd": random.random()
        }

        video_url_headers = headers.copy()
        video_url_headers["Accept"] = "application/json, text/javascript, */*; q=0.01"
        video_url_headers["Referer"] = detail_url
        video_url_headers["X-Requested-With"] = "XMLHttpRequest"

        video_info = session.get(
            url=get_video_url,
            params=params,
            headers=video_url_headers
        ).json()

        video_url_list.append({
            "filename": name,
            "url": get_real_url(video_info['videoInfo']['videos']['srcUrl'], cont_id)
        })

    def download_video(video_info):
        print(video_info['url'], video_info['filename'], '下载中！')
        video_headers = headers.copy()
        video_headers['Host'] = 'video.pearvideo.com'
        video_headers['method'] = 'GET'
        video_headers['path'] = urlparse(video_info['url']).path
        video_headers['Accept'] = '*/*'
        video_headers['Accept-Encoding'] = 'identity;q=1, *;q=0'
        video_headers['Accept-Language'] = 'zh-CN,zh;q=0.9'
        video_headers["Range"] = "bytes=0-"
        video_headers["Referer"] = host
        video_headers["Sec-Ch-Ua"] = 'Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114'
        video_headers["Sec-Fetch-Dest"] = 'video'
        video_headers["Sec-Ch-Ua-Mobile"] = '?0'
        video_headers["Sec-Ch-Ua-Platform"] = 'Windows'
        video_headers["Sec-Fetch-Mode"] = "no-cors"
        video_headers["Sec-Fetch-Site"] = "same-site"
        video_res = session.get(
            url=video_info['url'], headers=video_headers)
        print(video_info['filename'], '下载成功！')
        with open(video_info['filename'], 'wb') as fp:
            fp.write(video_res.content)
            print(video_info['filename'], '写入成功！')
        return True

    video_download_pool = Pool(4)
    video_download_pool.map(download_video, video_url_list)

#  B: Math.round(+new Date / 1E3),

    # mt.lang.find = function(a, b, k) {
    #     if (mt.lang.isArray(a) & & mt.lang.j(b))
    #     for (var d=a.length, f=0
    #          f < d
    #          f++)
    #     if (f in a & & b.call(k | | a, a[f], f))
    #     return a[f]
    #     return u
    # }

    # mt.lang.X = function(a, b) {
    #     return mt.lang.find(a, function(k) {
    #         return k === b
    #     }) != u
    # }
