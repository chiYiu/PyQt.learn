# -*- coding: utf-8 -*-
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

        self.label_v_layout = QVBoxLayout()
        self.line_v_layout = QVBoxLayout()
        self.button_h_layout = QHBoxLayout()
        self.label_line_h_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.label_v_layout.addWidget(self.user_label)
        self.label_v_layout.addWidget(self.pwd_label)
        self.line_v_layout.addWidget(self.user_line)
        self.line_v_layout.addWidget(self.pwd_line)
        self.button_h_layout.addWidget(self.login_button)
        self.button_h_layout.addWidget(self.signin_btton)
        self.label_line_h_layout.addLayout(self.label_v_layout)
        self.label_line_h_layout.addLayout(self.line_v_layout)
        self.all_v_layout.addLayout(self.label_line_h_layout)
        self.all_v_layout.addLayout(self.button_h_layout)

        self.setLayout(self.all_v_layout)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())