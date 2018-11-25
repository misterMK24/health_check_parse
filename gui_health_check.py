import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QLineEdit, QStyle, QFileDialog)
from PyQt5 import QtGui
import os
import re
from hcf import dir_working

# hcf - functions to parse file and going through dir

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Application")
        # self.resize(300, 300)
        self.setFixedSize(250, 250)

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
        global namedir
        namedir = QFileDialog.getExistingDirectory(self, 'Выберите директорию')


    def OkPressed(self):
        command_name = self.input_text1.text()
        dir_working(namedir, command_name)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    ico = window.style().standardIcon(QStyle.SP_ArrowForward)
    window.setWindowIcon(ico)
    sys.exit(app.exec_())
