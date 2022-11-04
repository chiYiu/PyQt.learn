# -*- coding: utf-8 -*-
import sys
from PySide.QtGui import QApplication,QWidget,QDialog,QLabel,QLineEdit,QPushButton,\
						QGridLayout,QVBoxLayout,QHBoxLayout,QMessageBox
#完善单行文本输入框和按钮功能

USER_PWD = {
		'zhangpeilin': '123456'
	}#全局变量USER_PWD,检查账号密码

class Demo(QWidget):
	"ocstring for Demo"""
	def __init__(self):
		super(Demo, self).__init__()
		self.resize(300,180)

		self.user_label = QLabel('Username:',self)
		self.pwd_label = QLabel('Password:',self)
		self.user_line = QLineEdit(self)
		self.pwd_line = QLineEdit(self)
		self.login_button = QPushButton('Log in',self)
		self.signin_button = QPushButton('Sign in',self)

		self.grid_layout = QGridLayout()
		self.h_layout = QHBoxLayout()
		self.v_layout = QVBoxLayout()

		self.layout_init()
		self.lineedit_init()
		self.pushButton_init()

	def layout_init(self):#窗口布局
		self.grid_layout.addWidget(self.user_label,0,0,1,1)
		self.grid_layout.addWidget(self.pwd_label,1,0,1,1)
		self.grid_layout.addWidget(self.user_line,0,1,1,1)
		self.grid_layout.addWidget(self.pwd_line,1,1,1,1)
		self.h_layout.addWidget(self.login_button)
		self.h_layout.addWidget(self.signin_button)
		self.v_layout.addLayout(self.grid_layout)
		self.v_layout.addLayout(self.h_layout)

		self.setLayout(self.v_layout)

	def lineedit_init(self):#setPlaceholderText()方法实现占位字符
		self.user_line.setPlaceholderText('Please enter your username')
		self.pwd_line.setPlaceholderText('Please enter your password')

		self.user_line.textChanged.connect(self.check_input_func)
		self.pwd_line.textChanged.connect(self.check_input_func)

	def check_input_func(self):#检查输入框
		if self.user_line.text() and self.pwd_line.text():
			self.login_button.setEnabled(True)
		else:
			self.login_button.setEnabled(False)

	def pushButton_init(self):#输入密前默认关闭按钮并连接密码检查函数
		self.login_button.setEnabled(False)
		self.login_button.clicked.connect(self.check_login_func)

	def check_login_func(self):#账号密码密码检查函数
		if USER_PWD.get(self.user_line.text()) == self.pwd_line.text():
			QMessageBox.information(self,'Information','Log in Successfully!')
		else:
			QMessageBox.critical(self,'Wrong','Wrong Username or Password!')

		self.user_line.clear()
		self.pwd_line.clear()
if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo=Demo()
	demo.show()
	sys.exit(app.exec_())