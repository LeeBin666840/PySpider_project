import datetime
import os
import sys
import random

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QDateTimeEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtWidgets import QStyleFactory


class AppWidget(QWidget):
    """程序界面设定控制类"""

    def __init__(self):
        # 调用父类的初始化方法
        super().__init__()
        # 调用界面初始化方法（一般会将UI界面的代码封装到另外一个方法函数中，而不直接放到__init__）
        self.init_ui()
        # 加载文件中存储的所有人员信息
        self.load_all_infos()

    def init_ui(self):
        """设置UI界面"""
        self.setWindowTitle("人员管理系统——WuYan")
        self.setFixedSize(1220, 771)

        # 创建字体对象，用来对要显示的文字进行设定
        font = QtGui.QFont()
        font.setFamily("黑体")

        
        font.setPointSize(12)

        # 姓名
        label_name = QLabel(self)
        label_name.setGeometry(40, 30, 54, 16)
        label_name.setText("姓名：")
        label_name.setFont(font)
        self.line_edit_name = QLineEdit(self)
        self.line_edit_name.setGeometry(90, 30, 141, 20)

        # 性别
        label_gender = QLabel(self)
        label_gender.setGeometry(270, 30, 54, 16)
        label_gender.setFont(font)
        label_gender.setText("性别：")
        self.line_edit_gender = QComboBox(self)
        self.line_edit_gender.setGeometry(340, 30, 201, 20)
        self.line_edit_gender.addItems(['男', '女'])

        # 身份证
        label_id = QLabel(self)
        label_id.setGeometry(580, 30, 54, 16)
        label_id.setFont(font)
        label_id.setText("身份证：")
        self.line_edit_id = QLineEdit(self)
        self.line_edit_id.setGeometry(660, 30, 221, 20)
        # 地址
        label_addr = QLabel(self)
        label_addr.setGeometry(40, 110, 54, 16)
        label_addr.setFont(font)
        label_addr.setText("地址：")
        self.line_edit_addr = QLineEdit(self)
        self.line_edit_addr.setGeometry(92, 110, 141, 20)

        # 电话
        label_phone = QLabel(self)
        label_phone.setGeometry(270, 70, 54, 16)
        label_phone.setFont(font)
        label_phone.setText("电话:")
        self.line_edit_phone = QLineEdit(self)
        self.line_edit_phone.setGeometry(340, 70, 201, 20)

        # 部门
        label_department = QLabel(self)
        label_department.setGeometry(590, 70, 54, 16)
        label_department.setFont(font)
        label_department.setText("部门:")
        self.line_edit_department = QLineEdit(self)
        self.line_edit_department.setGeometry(660, 70, 221, 20)

        # 出生日期
        label_birthdate = QLabel(self)
        label_birthdate.setGeometry(580, 110, 81, 16)
        label_birthdate.setFont(font)
        label_birthdate.setText("出生日期：")
        self.line_edit_birthday = QDateTimeEdit(self)
        self.line_edit_birthday.setGeometry(670, 110, 211, 20)
        self.line_edit_birthday.setCalendarPopup(True)
        self.line_edit_birthday.setDisplayFormat("yyyy-MM-dd")

        # 专业
        label_skill = QLabel(self)
        label_skill.setGeometry(40, 70, 51, 16)
        label_skill.setFont(font)
        label_skill.setText("专业：")
        self.line_edit_skill = QLineEdit(self)
        self.line_edit_skill.setGeometry(90, 70, 141, 20)

        # 职务
        label_post = QLabel(self)
        label_post.setGeometry(270, 110, 51, 16)
        label_post.setFont(font)
        label_post.setText("职务：")
        self.line_edit_post = QLineEdit(self)
        self.line_edit_post.setGeometry(340, 110, 201, 20)

        # 备注
        label_note = QLabel(self)
        label_note.setGeometry(40, 150, 51, 16)
        label_note.setFont(font)
        label_note.setText("备注：")
        self.text_edit_note = QTextEdit(self)
        self.text_edit_note.setGeometry(90, 150, 381, 71)

        # btn：录入信息
        btn_add_info = QPushButton(self)
        btn_add_info.setGeometry(580, 190, 75, 23)
        btn_add_info.setText("录入信息")
        # 事件绑定
        btn_add_info.clicked.connect(self.add_new_student_info)

        # btn：修改信息
        self.btn_change = QPushButton("修改信息", self)
        self.btn_change.setGeometry(700, 190, 75, 23)
        self.btn_change.setVisible(False)
        # 事件绑定
        self.btn_change.clicked.connect(self.save_change_info)

        # 人员信息表
        self.table_infos = QTableWidget(self)
        self.table_infos.setGeometry(10, 350, 1200, 411)
        self.table_infos.setColumnCount(11)
        self.table_infos.setHorizontalHeaderLabels([
            '编号', '姓名', '性别', '身份证', '专业', '电话', '部门', '地址', '职务', '出生日期', '备注'
        ])
        # 禁用双击编辑单元格
        self.table_infos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 改为选择一行
        self.table_infos.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 添加右击菜单
        self.table_infos.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table_infos.customContextMenuRequested.connect(self.generate_menu)

        # 隐藏的文本框，用来存储编号
        self.person_no = QLineEdit(self)
        self.person_no.setGeometry(90, 220, 141, 20)
        self.person_no.setVisible(False)

        # btn：查看全部
        self.btn_find_all = QPushButton(self)
        self.btn_find_all.setGeometry(74, 290, 81, 23)
        self.btn_find_all.setText("查看全部")
        # 事件绑定
        self.btn_find_all.clicked.connect(self.get_all_infos)

        # 按类型查找
        self.label_find_type = QLabel(self)
        self.label_find_type.setGeometry(330, 295, 91, 16)
        self.label_find_type.setFont(font)
        self.label_find_type.setText("按类型查找")

        # 下拉菜单，查找类型
        self.select_btn = QComboBox(self)
        self.select_btn.setGeometry(420, 290, 111, 22)
        find_type = ["姓名", "性别", "身份证", "专业", "部门", "编号", "出生日期范围"]
        for i, type_temp in enumerate(find_type):
            self.select_btn.addItem("")
            self.select_btn.setItemText(i, type_temp)
        # 事件绑定
        self.select_btn.currentIndexChanged.connect(self.change_search_type)

        # 查找输入框
        self.line_edit_find = QLineEdit(self)
        self.line_edit_find.setGeometry(550, 290, 161, 20)

        # 查找日期范围（默认不显示，只有当选择查询日期范围时才显示）
        self.line_edit_star_time = QDateTimeEdit(self)
        self.line_edit_star_time.setGeometry(550, 290, 100, 20)
        self.line_edit_star_time.setCalendarPopup(True)
        self.line_edit_star_time.setDisplayFormat("yyyy-MM-dd")
        self.line_edit_star_time.setVisible(False)
        self.line_edit_end_time = QDateTimeEdit(self)
        self.line_edit_end_time.setGeometry(655, 290, 100, 20)
        self.line_edit_end_time.setCalendarPopup(True)
        self.line_edit_end_time.setDisplayFormat("yyyy-MM-dd")
        self.line_edit_end_time.setVisible(False)

        # btn：查找
        self.btn_find = QPushButton(self)
        self.btn_find.setGeometry(780, 290, 75, 23)
        self.btn_find.setText("查找")
        # 事件绑定
        self.btn_find.clicked.connect(self.search_info_from_files)

    def change_search_type(self):
        """更改搜索类型"""
        search_type = self.select_btn.currentText()
        if search_type == '出生日期范围':
            self.line_edit_star_time.setVisible(True)
            self.line_edit_end_time.setVisible(True)
            self.line_edit_find.setVisible(False)
        else:
            self.line_edit_star_time.setVisible(False)
            self.line_edit_end_time.setVisible(False)
            self.line_edit_find.setVisible(True)

    def get_all_infos(self):
        """查询所有人员信息并显示"""
        self.load_all_infos()
        # 清理查询输入框内容
        self.line_edit_find.setText("")

    def search_info_from_files(self):
        # 查询类型
        search_type = self.select_btn.currentText()

        if search_type == '出生日期范围':
            start_time = self.line_edit_star_time.text().split('-')
            stop_time = self.line_edit_end_time.text().split('-')
            start_time = datetime.date(int(start_time[0]), int(start_time[1]), int(start_time[2]))
            stop_time = datetime.date(int(stop_time[0]), int(stop_time[1]), int(stop_time[2]))
            if (stop_time - start_time).days < 0:
                QMessageBox.information(self, '提示', '开始日期不能小于结束日期')
                return

        # 从文件中读取所有的信息
        all_infos = []
        with open("infos.txt", 'r+', encoding='utf-8') as f:
            info_lines = f.readlines()
            for temp in info_lines:
                all_infos.append(temp.replace('\n', ''))

        # 获取要搜索的内容
        search_content = self.line_edit_find.text()

        # 存放搜索结果
        search_result = []
        for temp_info in all_infos:
            info = temp_info.split(",")
            if search_type == '姓名' and search_content == info[1]:
                search_result.append(temp_info)
            if search_type == '性别' and search_content == info[2]:
                search_result.append(temp_info)
            if search_type == '编号' and search_content == info[0]:
                search_result.append(temp_info)
            if search_type == '身份证' and search_content == info[3]:
                search_result.append(temp_info)
            if search_type == '专业' and search_content == info[4]:
                search_result.append(temp_info)
            if search_type == '部门' and search_content == info[6]:
                search_result.append(temp_info)
            if search_type == '出生日期范围':
                start_time_temp = datetime.datetime.strptime(str(start_time), '%Y-%m-%d')
                stop_time_temp = datetime.datetime.strptime(str(stop_time), '%Y-%m-%d')
                date_search = datetime.datetime.strptime(info[9], '%Y-%m-%d')
                if start_time_temp <= date_search <= stop_time_temp:
                    search_result.append(temp_info)

        # 填充查询到的信息到表中
        info_count = len(search_result)
        self.table_infos.setRowCount(info_count)
        for i, temp in enumerate(search_result):
            for j, temp_item in enumerate(temp.split(",")):
                new_item = QTableWidgetItem(temp_item)
                new_item.setTextAlignment(Qt.AlignHCenter)
                self.table_infos.setItem(i, j, new_item)

    def save_change_info(self):
        """修改数据"""
        person_no = self.person_no.text()
        name = self.line_edit_name.text()
        gender = self.line_edit_gender.currentText()
        ids = self.line_edit_id.text()
        skill = self.line_edit_skill.text()
        phone = self.line_edit_phone.text()
        department = self.line_edit_department.text()
        addr = self.line_edit_addr.text()
        post = self.line_edit_post.text()
        birthday = self.line_edit_birthday.text()
        note = self.text_edit_note.toPlainText()

        infos = [person_no, name, gender, ids, skill, phone, department, addr, post, birthday, note]
        if "" in infos:
            QMessageBox.information(self, '提示', '修改的信息不能为空')

        all_infos = []
        with open("infos.txt", 'r+', encoding='utf-8') as f:
            info_lines = f.readlines()
            for temp in info_lines:
                all_infos.append(temp.replace('\n', ''))

        for i in range(len(all_infos)):
            temp_person_no = all_infos[i].split(",")[0]
            if person_no == str(temp_person_no):
                all_infos[i] = ",".join(infos)
                break

        with open("infos.txt", 'w', encoding='utf-8') as f:
            for text in all_infos:
                f.write(text + '\n')

        # 清空文本框的内容
        self.person_no.setText('')
        self.line_edit_name.setText('')
        self.line_edit_id.setText('')
        self.line_edit_skill.setText('')
        self.line_edit_phone.setText('')
        self.line_edit_department.setText('')
        self.line_edit_addr.setText('')
        self.line_edit_post.setText('')
        self.text_edit_note.setPlainText('')

        # 重新加载所有信息
        self.reload_all_infos()

        QMessageBox.information(self, '提示', '修改成功')

    def generate_menu(self, pos):
        """右键菜单"""
        menu = QMenu()
        item1 = menu.addAction("修改")
        item2 = menu.addAction("删除")
        action = menu.exec_(self.table_infos.mapToGlobal(pos))
        if action == item1:
            print("选择了'修改'操作")

            # 显示“修改信息按钮”
            self.btn_change.setVisible(True)

            # 从表格中提取需要的数据
            table_selected_index = self.table_infos.currentIndex().row()
            model = self.table_infos.model()
            person_no = model.data(model.index(table_selected_index, 0))
            name = model.data(model.index(table_selected_index, 1))
            gender = model.data(model.index(table_selected_index, 2))
            ids = model.data(model.index(table_selected_index, 3))
            skill = model.data(model.index(table_selected_index, 4))
            phone = model.data(model.index(table_selected_index, 5))
            department = model.data(model.index(table_selected_index, 6))
            addr = model.data(model.index(table_selected_index, 7))
            post = model.data(model.index(table_selected_index, 8))
            birthday = model.data(model.index(table_selected_index, 9))
            note = model.data(model.index(table_selected_index, 10))

            # 将这些数据设置到对应的文本框
            self.line_edit_name.setText(name)
            if gender == '男':
                self.line_edit_gender.setItemText(0, gender)
                self.line_edit_gender.setItemText(1, '女')
            else:
                self.line_edit_gender.setItemText(0, gender)
                self.line_edit_gender.setItemText(1, '男')
            # 用一个隐藏的文本框记录要修改的人员编号
            self.person_no.setText(person_no)
            self.line_edit_id.setText(ids)
            self.line_edit_skill.setText(skill)
            self.line_edit_phone.setText(phone)
            self.line_edit_department.setText(department)
            self.line_edit_addr.setText(addr)
            self.line_edit_post.setText(post)
            self.line_edit_birthday.setDate(QDate.fromString(birthday, "yyyy-MM-dd"))
            self.text_edit_note.setPlainText(note)
        elif action == item2:
            print("选择了'删除'操作")
            table_selected_index = self.table_infos.currentIndex().row()
            # 获取表格数据模型对象
            model = self.table_infos.model()
            # 通过模型对象提取第X行第0列（即编号）单元格对象
            table_selected_first_cell = model.index(table_selected_index, 0)
            # 提取编号数据
            person_no = model.data(table_selected_first_cell)
            print("要删除的编号:", person_no)

            all_infos = []
            with open("infos.txt", 'r+', encoding='utf-8') as f:
                all_student_info_lines = f.readlines()
                for students_info_line in all_student_info_lines:
                    all_infos.append(students_info_line.replace('\n', ''))

            for i in range(len(all_infos)):
                temp_student_id = all_infos[i].split(",")[0]
                if person_no == str(temp_student_id):
                    all_infos.remove(all_infos[i])
                    break

            with open("infos.txt", 'w', encoding='utf-8') as f:
                for text in all_infos:
                    f.write(text + '\n')

            # 重新加载所有信息
            self.reload_all_infos()

            QMessageBox.information(self, '提示', '删除成功')

    def reload_all_infos(self):
        """重新加载所有信息"""
        self.load_all_infos()

    def add_new_student_info(self):
        name = self.line_edit_name.text()
        gender = self.line_edit_gender.currentText()
        ids = self.line_edit_id.text()
        skill = self.line_edit_skill.text()
        phone = self.line_edit_phone.text()
        department = self.line_edit_department.text()
        addr = self.line_edit_addr.text()
        post = self.line_edit_post.text()
        birthday = self.line_edit_birthday.text()
        note = self.text_edit_note.toPlainText()
        print("name", name)
        print("gender", gender)
        print("ids", ids)
        print("skill", skill)
        print("phone", phone)
        print("department", department)
        print("addr", addr)
        print("post", post)
        print("birthday", birthday)
        print("note", note)

        # 判断有没有填写的信息，如果有则提示，如果没有则存储到文件
        infos = [name, gender, ids, skill, phone, department, addr, post, birthday, note]
        if "" in infos:
            QMessageBox.information(self, '提示', '输入的信息不能为空')
        else:
            person_no = random.randint(10000, 99999)
            infos.insert(0, str(person_no))
            infos_str = ",".join(infos)
            with open('infos.txt', 'a+', encoding='utf-8') as f:
                f.write(infos_str + '\n')
                f.close()

            # 重新加载所有信息
            self.reload_all_infos()

            QMessageBox.information(self, '提示', '提交成功')

    def load_all_infos(self):
        """加载所有的人员信息"""
        path = 'infos.txt'
        # 1. 判断是否存储文件，如果不存在则函数结束
        if not os.path.exists(path):
            return

        # 2. 加载所有数据
        all_infos = list()
        with open(path, 'r', encoding='utf-8') as f:
            infos_list = f.readlines()
            for stu_info in infos_list:
                all_infos.append(stu_info.replace('\n', ''))

        # 3. 填充到信息表中
        infos_count = len(all_infos)
        self.table_infos.setRowCount(infos_count)
        for i, temp_info in enumerate(all_infos):
            for j, info_item in enumerate(temp_info.split(",")):
                new_item = QTableWidgetItem(info_item)
                new_item.setTextAlignment(Qt.AlignHCenter)
                self.table_infos.setItem(i, j, new_item)


if __name__ == '__main__':
    # 创建应用程序对象
    app = QApplication(sys.argv)

    # 设置窗口窗口风格
    QApplication.setStyle(QStyleFactory.create("Fusion"))
    print(QStyleFactory.keys())

    # 创建一个要显示的窗口对象
    app_widget = AppWidget()
    app_widget.show()

    # 让应用程序一直运行，在这期间会显示UI界面、检测事件等操作
    sys.exit(app.exec())


