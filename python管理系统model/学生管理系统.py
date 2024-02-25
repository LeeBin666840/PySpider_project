"""
-*- coding: utf-8 -*-
@Time    : 2023/4/25 13:27
@Author  : 无言
@FileName: 学生管理系统.py
@Software: PyCharm
"""
msg = """*******************************************************
欢迎使用【学生信息管理系统】v1.0
请选择你想要进行的操作
1.新建学生信息
2.显示全部信息
3.查询学生信息
4.删除学生信息
5.修改学生信息

6.退出系统
*******************************************************"""
# 创建基本学生信息放在字典里
student_info = [
    {'姓名': '多乐', '语文': 80, '数学': 60, '英语': 60, '总分': 200},
    {'姓名': '小九', '语文': 80, '数学': 60, '英语': 60, '总分': 200},
    {'姓名': '彦松', '语文': 80, '数学': 60, '英语': 60, '总分': 200},
]
while True:
    print(msg)
    # 选择序号输入操作
    num = input('请输入你操作序号:')
    # 判断输入内容是什么，根据不同操作情况，进入不同界面
    if num == '1':
        print('新建学生信息')
        # 输入相应的数据内容
        name = input('请输入学生姓名:')
        chinese = input('请输入学生语文成绩:')
        math = input('请输入学生数学成绩:')
        english = input('请输入学生英语成绩:')
        score = int(chinese) + int(math) + int(english)
        student_dict = {
            '姓名': name,
            '语文': chinese,
            '数学': math,
            '英语': english,
            '总分': score,
        }
        # 列表添加元素
        student_info.append(student_dict)
    elif num == '2':
        print('显示全部信息')
        print('姓名\t\t语文\t\t数学\t\t英语\t\t总分')
        for student in student_info:
            print(
                student['姓名'] + '\t\t' +
                str(student['语文']) + '\t\t' +
                str(student['数学']) + '\t\t' +
                str(student['英语']) + '\t\t' +
                str(student['总分']) + '\t\t'
            )
    # 查询学生信息
    elif num == '3':
        print('查询学生信息')
        name = input('请输入学生姓名:')
        for student in student_info:
            # 判断是否有这个学生
            if student['姓名'] == name:
                print('姓名\t\t语文\t\t数学\t\t英语\t\t总分')
                print(
                    student['姓名'] + '\t\t' +
                    str(student['语文']) + '\t\t' +
                    str(student['数学']) + '\t\t' +
                    str(student['英语']) + '\t\t' +
                    str(student['总分']) + '\t\t'
                )
                break
        else:
            print('查无此人！！')
    elif num == '4':
        print('删除学生信息')
        name = input('请输入学生姓名:')
        for student in student_info:
            # 判断是否有这个学生
            if student['姓名'] == name:
                print('姓名\t\t语文\t\t数学\t\t英语\t\t总分')
                print(
                    student['姓名'] + '\t\t' +
                    str(student['语文']) + '\t\t' +
                    str(student['数学']) + '\t\t' +
                    str(student['英语']) + '\t\t' +
                    str(student['总分']) + '\t\t'
                )
                word=input('是否要开除这个学生（y/n）:')
                if word == 'y' or word=='Y':
                    # 删除学生信息，相当于删除列表里面元素
                    student_info.remove(student)
                elif word=='n' or word == 'N':
                    break
                else:
                    print('操作失误')
                break
        else:
            print('查无此人！！')
    elif num == '5':
        print('修改学生信息')
        name = input('请输入学生姓名:')
        for student in student_info:
            # 判断是否有这个学生
            if student['姓名'] == name:
                print('姓名\t\t语文\t\t数学\t\t英语\t\t总分')
                print(
                    student['姓名'] + '\t\t' +
                    str(student['语文']) + '\t\t' +
                    str(student['数学']) + '\t\t' +
                    str(student['英语']) + '\t\t' +
                    str(student['总分']) + '\t\t'
                )
                word = input('是否要修改这个学生（y/n）:')
                if word == 'y' or word == 'Y':
                    name = input('请输入学生姓名:')
                    chinese = input('请输入学生语文成绩:')
                    math = input('请输入学生数学成绩:')
                    english = input('请输入学生英语成绩:')
                    score = int(chinese) + int(math) + int(english)
                    # 字符修改值
                    student['姓名']=name
                    student['语文']=chinese
                    student['数学']=math
                    student['英语']=english
                    student['总分']=score
                    print(f'{student["姓名"]}信息修改成功....')

                elif word == 'n' or word == 'N':
                    continue
                else:
                    print('操作失误')
                break
        else:
            print('查无此人！！')
    elif num == '0':
        print('退出系统')
        break
    else:
        print('输入序号有误，请正确输入内容')
