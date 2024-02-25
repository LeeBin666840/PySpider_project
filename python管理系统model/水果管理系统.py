
def meun():
    menu_info = '''＋－－－－－－－水果管理系统－－－－－－－＋
    ｜ 1）添加水果信息 
    ｜ 2）显示所有水果的信息 
    ｜ 3）删除水果信息 
    ｜ 4）修改水果信息 
    ｜ 5）按含水量高－低显示水果信息 
    ｜ 6）按含水量低－高显示水果信息 
    ｜ 7）按VC含量高－低显示水果信息 
    ｜ 8）按VC含量低－高显示水果信息 
    ｜ 9）保存水果信息到文件（fruit.txt) 
    ｜ 10）从文件中读取水果数据（fruit.txt) 
    ｜ 退出：其他任意按键＜回车＞ 
＋－－－－－－－－－－－－－－－－－－－－－－＋
    '''
    print(menu_info)


# 用于sorted排序
def get_water(*l):
    for x in l:
        return x.get("water")


def get_vc(*l):
    for x in l:
        return x.get("vc")


# 1)添加水果信息
def add_fruit_info():
    # 用列表存储水果信息,返回值为该列表
    L = []
    while True:
        n = input("请输入水果名字：")
        # 名字为空,跳出循环
        if not n:
            break
        # 捕获异常
        try:
            w = int(input("请输入含水量(ml/100g)："))
            v = int(input("请输入VC含量(ml/100g)："))
        except:
            print("输入无效，不是整形数值．．．．重新录入信息")
            continue
        # 用字典形式易于提取想要的信息
        info = {"name": n, "water": w, "vc": v}

        L.append(info)
    print("水果信息录入完毕！！！")
    return L


# 2)显示所有水果的信息
def show_fruit_info(fruit_info):
    if not fruit_info:
        print("无数据信息．．．．．")
        return
    print("名字".center(8), "含水量".center(4), "VC含量".center(4))
    for info in fruit_info:
        print(info.get("name").center(8) + str(info.get("water")).center(12) + str(info.get("vc")).center(4))


# 3)删除水果信息
def del_fruit_info(fruit_info, del_name=''):
    if not del_name:
        del_name = input("请输入删除的水果名称：")
    for info in fruit_info:
        if del_name == info.get("name"):
            return info
        # 异常处理
        raise IndexError("水果名称不匹配,没有找到%s" % del_name)


# 4)修改水果信息
def mod_fruit_info(fruit_info):
    mod_name = input("请输入修改的水果名称：")
    for info in fruit_info:
        if mod_name == info.get("name"):
            w = int(input("请输入修改后的含水量："))
            v = int(input("请输入修改后的VC含量："))
            info = {"name": mod_name, "water": w, "vc": v}
    return info
    raise IndexError("水果信息不匹配,没有找到%s" % mod_name)


# 5)按含水量高－低显示水果信息
def water_reduce(fruit_info):
    print("按含水量高－低显示")
    mit = sorted(fruit_info, key=get_water, reverse=True)
    show_fruit_info(mit)


# 6)按含水量低－高显示水果信息
def water_rise(fruit_info):
    print("按含水量低－高显示")
    mit = sorted(fruit_info, key=get_water)
    show_fruit_info(mit)


# 7)按VC含量高－低显示水果信息
def vc_reduce(fruit_info):
    print("按VC含量高－低显示：")
    mit = sorted(fruit_info, key=get_vc, reverse=True)
    show_fruit_info(mit)


# 8)按VC含量低－高显示水果信息
def vc_rise(fruit_info):
    print("按VC含量低－高显示：")
    mit = sorted(fruit_info, key=get_vc)
    show_fruit_info(mit)


# 9)保存水果信息到文件（students.txt)
def save_info(fruit_info):
    try:
        fruit_txt = open("fruit.txt", "w")  # 以写模式打开，并清空文件内容
    except Exception as e:
        fruit_txt = open("fruit.txt", "x")  # 文件不存在，创建文件并打开
    for info in fruit_info:
        fruit_txt.write(str(info) + "\n")  # 按行存储，添加换行符
    # 关闭文件
    fruit_txt.close()


# 10)从文件中读取数据
def read_info():
    old_info = []
    try:
        fruit_txt = open("fruit.txt")
    except:
        print("暂未保存数据信息")  # 打开失败，文件不存在说明没有数据保存
        return
    while True:
        info = fruit_txt.readline()
        if not info:
            break
        info = info.rstrip()  # 去掉换行符
        info = info[1:-1]  # 去掉｛｝
        print(info)
    # 关闭文件
    fruit_txt.close()


def main():
    # 用列表存储数据
    fruit_info = []
    while True:
        meun()
        number = input("请输入选项：")
        # 根据所输入的数字进入不同的功能(函数)
        if number == '1':
            fruit_info = add_fruit_info()
        elif number == '2':
            show_fruit_info(fruit_info)
        elif number == '3':
            try:
                fruit_info.remove(del_fruit_info(fruit_info))
            except Exception as e:
                # 水果名字不匹配
                print(e)
        elif number == '4':
            try:
                fruit = mod_fruit_info(fruit_info)
            except Exception as e:
                # 水果名字不匹配
                print(e)
            else:
                # 首先根据输入信息的名字，从列表中删除该信息，然后重新添加该水果最新信息
                fruit_info.remove(del_fruit_info(fruit_info, del_name=fruit.get("name")))
                fruit_info.append(fruit)
        elif number == '5':
            water_reduce(fruit_info)
        elif number == '6':
            water_rise(fruit_info)
        elif number == '7':
            vc_reduce(fruit_info)
        elif number == '8':
            vc_rise(fruit_info)
        elif number == '9':
            save_info(fruit_info)
        elif number == '10':
            fruit_info = read_info()
        else:
            break
        input("回车显示菜单")

main()