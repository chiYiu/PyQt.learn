# -*- coding: utf-8 -*-
import sys
from PySide.QtGui import QApplication,QWidget,QLabel,QLineEdit,QPushButton,\
                        QVBoxLayout,QHBoxLayout,QGridLayout


class Demo(QWidget):
    """docstring for Demo"""
    def __init__(self):
        super(Demo, self).__init__()
        self.user_label = QLabel("Username:",self)
        self.pwd_label = QLabel("Password:",self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_button = QPushButton('Log in',self)
        self.signin_button = QPushButton('Sign in',self)



        self.grid_layout = QGridLayout()#实例化一个QGridLayout布局管理器
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.grid_layout.addWidget(self.user_label,0,0,1,1)#QGridLayout的addWidget()方法遵循
        self.grid_layout.addWidget(self.user_line,0,1,1,1)#addWidget(widget, row, column, rowSpan, columnSpan)
        self.grid_layout.addWidget(self.pwd_label,1,0,1,1)#widget控件，row为第几行，column为第几列，
        self.grid_layout.addWidget(self.pwd_line,1,1,1,1)#rowSpan表示控件去占用几行,columnSpan控件去占用几列
        self.h_layout.addWidget(self.login_button)
        self.h_layout.addWidget(self.signin_button)
        self.v_layout.addLayout(self.grid_layout)
        self.v_layout.addLayout(self.h_layout)


        self.setLayout(self.v_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())