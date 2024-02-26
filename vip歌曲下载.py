#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
------------------------
@author: 无言 
@time: 2024/1/27 13:40 
@file: vip歌曲下载.py
@project: PythonProject
Software: PyCharm
------------------------
"""
'''
欢迎大家来到顾老师直播间
一个专注于编程知识分享技术交流的学习直播

一、内容
python项目实战--第三方音乐数据采集

二、开发工具
解释器：python3.7
编辑器: pycharm专业版

三、教学时间
20:40-22:30

声音画面清晰度  1
'''
'''
技术栈:爬虫
- 概念：批量采集数据 / 模拟用户行为

一、项目思路分析
1.明确需求
- 目标: 音乐数据获取 
- 网址：https://www.gequbao.com/api/play_url?id=402856&json=1

2.抓包分析
<通过开发者工具数据来源分析>
①常规步骤：
 - f12: 打开开发者工具  
 - 网络面板:  进行数据监听和截获 
 - 刷新网页： 重新加载网页源码信息 得到音频内容
 - 音频链接： media 媒体音频
 https://sy-sycdn.kuwo.cn/0bf88da2e0ceafb5cd1a9d09af611f15/65b3aa0a/resource/n2/70/55/756351052.mp3?from=vip

②定位接口：找到音频链接来自哪里？
 - 复制音频随机一段参数
 - 点击放大镜搜索
 - 得到音频数据源链接

二、代码流程编写
1.发送请求 -> 模拟浏览器向url地址访问
 - https://www.gequbao.com/s/%E5%91%A8%E6%9D%B0%E4%BC%A6
2.获取数据 -> 得到网页源代码
3.解析数据 -> 提取id / 歌名 / 作者
4.二次请求 -> 模拟浏览器向单首歌曲接口请求
 - https://www.gequbao.com/api/play_url?id={xxx}&json=1
5.二次获取 -> 得到歌曲响应内容
6.二次解析 -> 提取音频连接
7.保存数据 -> 转格式之后进行下载

下载模块：
打开pycharm--> 找到终端<Terminal> --> 输入pip install 模块

年龄：30+  需求：兴趣 --》做兼职

六个月学习时间   永久更新学习

'''
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
