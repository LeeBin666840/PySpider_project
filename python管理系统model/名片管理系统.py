"""
名片管理系统
包含字段 : 姓名 职务  电话 地址
存储方式: 列表嵌套字典形式 <键存储名称，值存储对应名称的值>

"""
# 绘图说明存储方式
user_info = []
# 输入输出函数  input(谁是世界上最帅的男人:)  天上掉了一沓钞票，是不是要接受下
# if while 画执行的流程图
while True:

    print("""
    *****************************
        1. 添加名片
        2. 删除名片
        3. 修改名片
        4. 查询名片 (查询单一或所有)
    *****************************
    """)

    num = input("请输入功能序号: ")

    if num == "1":
        print("\n【添加名片】")
        name = input("请输入新姓名: ")
        gender = input("请输入职务: ")
        age = input("请输入电话: ")
        phone = input("请输入地址: ")

        user_info.append({"姓名": name, "职务": gender, "电话": age, "地址": phone})

    elif num == "2":
        print("\n【删除名片】")
        name = input("请输入要删除的姓名: ")
        for people in user_info:
            if people.get("姓名") == name:
                user_info.remove(people)

    elif num == "3":
        print("\n【修改名片】")
        name = input("请输入要修改的姓名: ")
        for people in user_info:
            if people.get("姓名") == name:
                name = input("请输入新姓名: ")
                gender = input("请输入职务: ")
                age = input("请输入电话: ")
                phone = input("请输入地址: ")
                people.update({"姓名": name, "职务": gender, "电话": age, "地址": phone})

    elif num == "4":
        print("\n【查询名片】")
        name = input("请输入要查询的姓名 (输入 all 查询所有): ")
        for people in user_info:
            if name == "all" or people.get("姓名") == name:
                print(people)

    else:
        print("功能错误")
