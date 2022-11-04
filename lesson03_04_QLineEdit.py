# -*- coding: utf-8 -*-
#上面的代码是将两个QLabel用垂直布局方式摆放，将两个QLineEdit也用垂直布局方式摆放，
#最后用一个水平布局管理来摆放着两个垂直布局管理器。那换种思路，
#可以把QLabel和QLineEdit用水平布局方式摆放：
import sys
from PySide.QtGui import QApplication,QWidget,QLabel,QLineEdit,QVBoxLayout,QHBoxLayout,QPushButton

class Demo(QWidget):
    """docstring for Demo"""
    def __init__(self):
        super(Demo, self).__init__()
        self.user_label = QLabel("Userrname:",self)
        self.pwd_label = QLabel("Password:",self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_button = QPushButton('Log in',self)
        self.signin_btton = QPushButton('sign in',self)

        self.user_h_layout = QHBoxLayout()
        self.pwd_h_layout = QHBoxLayout()
        self.button_h_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.user_h_layout.addWidget(self.user_label)
        self.user_h_layout.addWidget(self.user_line)
        self.pwd_h_layout.addWidget(self.pwd_label)
        self.pwd_h_layout.addWidget(self.pwd_line)
        self.button_h_layout.addWidget(self.login_button)
        self.button_h_layout.addWidget(self.signin_btton)
        self.all_v_layout.addLayout(self.user_h_layout)
        self.all_v_layout.addLayout(self.pwd_h_layout)
        self.all_v_layout.addLayout(self.button_h_layout)

        self.setLayout(self.all_v_layout)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())