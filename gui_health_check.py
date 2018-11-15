import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QLineEdit, QStyle, QFileDialog)
from PyQt5 import QtGui
import os
import re

class HealthCheckFIle:


    def __init__(self, command_name, dir):
        print("Here a new class")
        self.dir_working()
        # global command_name
        # command_name = input("Enter command: ")


    def get_dir(self):
        global dir_name
        global filename
        filename = 'CPaudit_HealthCheck.txt'
        # dir_name = input("Input a necessary dir: ")      # 'C:\Трансгаз Казань\Аудит_2018\ЗСПД'
        os.chdir(dir_name)
        dir_list = os.listdir(dir_name)
        return dir_list
        # print(os.listdir())


    def parse_file(self):
        index = 0
        result_string = []
        # command = input("Enter command: ")
        with open(filename, 'r') as file:
            for line in file:
                match_command = re.match(r'={3}\s' + command_name + r'\s[=]{3}', line)
                if match_command or index == 1:
                    index = 1
                    if re.match(r'={3}\s{1}[^=]+[=]{3}', line) and not match_command:
                        break
                    result_string.append(line)
        return result_string
        # self.to_file(result_string)


    def to_file(self, result_string, gw_name):
        with open('C:\\results\\python_parse.txt', 'a+') as file:
            file.write(gw_name + "\n")
            for string in result_string:
                file.write(string)


    def dir_working(self, command_name, dir):
        dir_list = self.get_dir()
        # result_string :str
        for gw_name in dir_list:
            # check_pasing = re.search(r'[.]{1}\w+', dir)
            # is this a dir?
            check_dir = dir_name + "\\" + gw_name
            if os.path.isdir(check_dir):                                     # re.search(r'[.]{1}\w+', dir) is None:
                # dir_for_gw = dir_name + '\\' + gw_name
                os.chdir(check_dir)                 # переходим в директорию
                current_dir = os.listdir(check_dir)    # поиск CPaudit_HealthCheck.txt

                if current_dir:                         # если директория не пуста
                    for in_dir in current_dir:
                        if re.fullmatch(r'\b[Ff]w[_-]{1}\S+[^\.tar]', in_dir):
                            print("OK")
                        if re.search(filename, in_dir) is not None:     # если искомый файл существует, то парсим
                            result_string = self.parse_file()
                            self.to_file(result_string, gw_name)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Application")
        self.resize(300, 300)

        self.label1 = QLabel("Input the command: ")
        self.label2 = QLabel("Input the directory: ")

        self.input_text1 = QLineEdit()
        self.input_text1.setToolTip("без пробелов")
        self.input_text1.setToolTipDuration(1500)

        self.button1 = QPushButton("Выполнить")
        self.button2 = QPushButton("Choose...")


        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox1.addWidget(self.label1)
        self.hbox1.addWidget(self.input_text1)
        self.hbox2.addWidget(self.label2)
        self.hbox2.addWidget(self.button2)

        self.vbox1 = QVBoxLayout()
        self.vbox1.addLayout(self.hbox1)
        self.vbox1.addLayout(self.hbox2)
        self.vbox1.addWidget(self.button1)
        self.setLayout(self.vbox1)
        self.setupUI()

    def setupUI(self):
        self.button1.clicked.connect(self.OkPressed)
        self.button2.clicked.connect(self.ChoosePressed)


    def ChoosePressed(self):
        namedir = QFileDialog.getExistingDirectory(self, 'Выберите директорию')
        return namedir

    def OkPressed(self):
        command_name = self.input_text1.text()
        print(command_name)
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    ico = window.style().standardIcon(QStyle.SP_ArrowForward)
    window.setWindowIcon(ico)
    sys.exit(app.exec_())