# -*- coding: utf-8 -*-
import sys
from PySide.QtGui import QApplication,QWidget,QDialog,QLabel,QLineEdit,QPushButton,\
						QGridLayout,QVBoxLayout,QHBoxLayout,QMessageBox

USER_PWD = {
		'zhangpeilin': '123456'
	}#全局变量USER_PWD,检查账号密码

#完善注册界面布局及功能
class SigninPage(QDialog):				#新写一个类，并继承于QDialog(另一个毛坯房)
	"ocstring for SigninPage"""
	def __init__(self):
		super(SigninPage, self).__init__()

		self.signin_user_label = QLabel('Username:',self)
		self.signin_pwd_label = QLabel('Password:',self)
		self.signin_pwd2_label = QLabel('Password:',self)
		self.signin_user_line = QLineEdit(self)
		self.signin_pwd_line = QLineEdit(self)
		self.signin_pwd2_line = QLineEdit(self)
		self.signin_button = QPushButton('Sign in',self)

		self.user_h_layout = QHBoxLayout()
		self.pwd_h_layout = QHBoxLayout()
		self.pwd2_h_layout = QHBoxLayout()
		self.all_v_layout = QVBoxLayout()

		self.layout_init()
		self.lineedit_init()
		self.pushButton_init()

	def layout_init(self):#窗口布局
		self.user_h_layout.addWidget(self.signin_user_label)
		self.user_h_layout.addWidget(self.signin_user_line)
		self.pwd_h_layout.addWidget(self.signin_pwd_label)
		self.pwd_h_layout.addWidget(self.signin_pwd_line)
		self.pwd2_h_layout.addWidget(self.signin_pwd2_label)
		self.pwd2_h_layout.addWidget(self.signin_pwd2_line)

		self.all_v_layout.addLayout(self.user_h_layout)
		self.all_v_layout.addLayout(self.pwd_h_layout)
		self.all_v_layout.addLayout(self.pwd2_h_layout)
		self.all_v_layout.addWidget(self.signin_button)

		self.setLayout(self.all_v_layout)

	def lineedit_init(self):#setPlaceholderText()方法实现占位字符
		self.signin_user_line.textChanged.connect(self.check_input_func)
		self.signin_pwd_line.textChanged.connect(self.check_input_func)
		self.signin_pwd2_line.textChanged.connect(self.check_input_func)

	def check_input_func(self):#检查输入框
		if self.signin_user_line.text() and self.signin_pwd_line.text() and self.signin_pwd2_line.text():
			self.signin_button.setEnabled(True)
		else:
			self.signin_button.setEnabled(False)

	def pushButton_init(self):#输入密前默认关闭按钮并连接密码检查函数
		self.signin_button.setEnabled(False)
		self.signin_button.clicked.connect(self.check_signin_func)

	def check_signin_func(self):#账号密码密码检查函数
		if self.signin_pwd_line.text() != self.signin_pwd2_line.text():
			QMessageBox.critical(self,'Wrong','Two Passwords Typed Are Not Same!')
		elif self.signin_user_line.text() not in USER_PWD:
			USER_PWD[self.signin_user_line.text()] = self.signin_pwd_line.text()
			QMessageBox.information(self,'Information','Register Successfully!')
			self.close()
		else:
			QMessageBox.critical(self,'Wrong','This Username Has Been Registered!')

		self.signin_user_line.clear()
		self.signin_pwd_line.clear()
		self.signin_pwd2_line.clear()