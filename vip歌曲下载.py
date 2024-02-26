#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 导入爬虫请求模块
import requests
# 导入解析模块
from parsel import Selector
# 导入表格模块
from prettytable import PrettyTable
# 导入文件操作流
import os

if not os.path.exists('music'):
    os.mkdir('music')
key_name = input('请输入你想搜索的歌手or歌曲:')
# 1.定义网址
url = f'https://www.gequbao.com/s/{key_name}'
# 2.模拟浏览器 伪装headers
headers = {
    'Cache-Control': 'no-cache',
    'Cookie': 'Hm_lvt_c2b69091f94cb4368f25c28fc7c2d28c=1706184131,1706272768; Hm_lpvt_c2b69091f94cb4368f25c28fc7c2d28c=1706274303',
    'Pragma': 'no-cache',
    'Referer': 'https://www.gequbao.com/',
    'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}
# 3.发送请求
response = requests.get(url, headers=headers)
# 4.获取数据
# print(response.text)
# 5.解析数据
selector = Selector(response.text)
# 实例化表格对象
table = PrettyTable()
num = 0
info_list = []
table.field_names = ['序号', '歌曲', '歌手', '音乐id']
# 配置的选择器对象
rows = selector.css('.card-text .row')[1:]
for row in rows:
    title = row.css('.text-primary::text').get().strip()
    name = row.css('.text-success::text').get().strip()
    music_id = row.css('.col-5 a::attr(href)').get().split('/')[-1]
    table.add_row([num, title, name, music_id])
    info_list.append([num, title, name, music_id])
    num += 1
print(table)
# 下载器
while True:
    try:
        key = int(input("请输入你想下载的歌曲序号(按-1即可退出程序):"))
        if key == -1:
            break
        # 下载的信息
        downloads = info_list[key]
        sing_id = downloads[-1]
        name = downloads[1]
        singer = downloads[2]
        # print(sing_id)
        # 拼接歌曲的音乐链接
        music_url = f'https://www.gequbao.com/api/play_url?id={sing_id}&json=1'
        # 二次请求
        music_data = requests.get(music_url).json()
        # print(music_data)
        # 解析数据
        music = music_data['data']['url']
        # print('音频链接:', music)
        print(f'歌曲>>>{name}下载成功！！！')
        # 下载歌曲
        music_content = requests.get(music).content
        with open(f'music/{name}.mp3', 'wb') as f:
            f.write(music_content)
    except Exception as e:
        print('你输入的序号有误！请重新选择！\n', e)
