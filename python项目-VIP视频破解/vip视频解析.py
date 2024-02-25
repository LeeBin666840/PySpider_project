"""
-*- coding: utf-8 -*-
@Time    : 2023/4/2 15:43
@Author  : 无言
@FileName: vip视频解析.py
@Software: PyCharm
"""
# 实例网址：https://film.qq.com/film_all_list/allfilm.html?type=movie&sort=75
import tkinter as tk
import webbrowser
# 创建窗口
root=tk.Tk()
# 标题
root.title('无言--观影软件')
# 设置大小
root.geometry('800x400+200+200')
# 读取图片
img=tk.PhotoImage(file='封面.png')
def show():
    """
    自定义函数 按钮触发事件
    :return:
    """
    # 获取输入框的内容
    word=input_va.get()
    # 获取选择的接口
    num=num_int_va.get()
    # 判断第一个接口
    if num==1:
        link1='https://jx.xmflv.com/?url='+word
        # 打开视频网站进行播放
        webbrowser.open(link1)
    elif num==2:
        link2='https://www.administratorw.com/index/qqvod.php?url='+word
        webbrowser.open(link2)
    elif num==3:
        link3='https://jx.m3u8.tv/jiexi/?url='+word
        webbrowser.open(link3)
# pack() 垂直布局  Label 标签组件
tk.Label(root,image=img).pack()
# 设置标签框
choose_frame=tk.LabelFrame(root)
# fill='both' 填充  pady=10 Y轴间距，
choose_frame.pack(fill='both',pady=10)
# 设置文本标签
tk.Label(choose_frame,text='选择接口:',font=('宋体',20)).pack(side=tk.LEFT)
# 设置可变变量 --> 确定你点击哪一个
num_int_va=tk.IntVar()
# 设置默认选择第一个
num_int_va.set(1)
# 设置单选按钮  side=tk.LEFT 靠左对齐
tk.Radiobutton(choose_frame,text='①号通用vip引擎【严禁商用】',font=('宋体',10),variable=num_int_va,value=1).pack(side=tk.LEFT,pady=5)
tk.Radiobutton(choose_frame,text='②号通用vip引擎【严禁商用】',font=('宋体',10),variable=num_int_va,value=2).pack(side=tk.LEFT,pady=5)
tk.Radiobutton(choose_frame,text='③号通用vip引擎【严禁商用】',font=('宋体',10),variable=num_int_va,value=3).pack(side=tk.LEFT,pady=5)
# 创建第二个标签框
input_frame=tk.LabelFrame(root)
input_frame.pack(fill='both',pady=10)
# 设置播放地址文本标签
tk.Label(input_frame,text='播放地址:',font=('宋体',20)).pack(side=tk.LEFT)
# 设置可变变量
input_va=tk.StringVar()
# 设置输入框 relief 输入框样式设置 flat平滑
tk.Entry(input_frame,width=100,relief='flat',textvariable=input_va).pack(side=tk.LEFT,fill='both')
# 设置按钮
tk.Button(root,text='Go点击在线解析播放',font=('黑体',20),bg='#449d44',relief='flat',command=show).pack(fill='both')
# 展示窗口
root.mainloop()