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
		self.signin_page = SigninPage()#实例化SigninPage()

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
		self.pwd_line.setEchoMode(self.pwd_line.Password)

	def check_input_func(self):#检查输入框
		if self.user_line.text() and self.pwd_line.text():
			self.login_button.setEnabled(True)
		else:
			self.login_button.setEnabled(False)

	def pushButton_init(self):#输入密前默认关闭按钮并连接密码检查函数
		self.login_button.setEnabled(False)
		self.login_button.clicked.connect(self.check_login_func)

		self.signin_button.clicked.connect(self.show_signin_page_func)
		#sign in按钮的clicked信号和show_signin_page_func()槽函数进行连接

	def check_login_func(self):#账号密码密码检查函数
		if USER_PWD.get(self.user_line.text()) == self.pwd_line.text():
			QMessageBox.information(self,'Information','Log in Successfully!')
		else:
			QMessageBox.critical(self,'Wrong','Wrong Username or Password!')

		self.user_line.clear()
		self.pwd_line.clear()

	def show_signin_page_func(self):
		self.signin_page.exec_()
		#我们用exec_方法来执行注册界面,为什么要使用exec_而不是show()
		#若使用exec_()的话，那么显示出来的注册界面就是模态的
		#意思就是当前只能对该注册界面进行操作
		#只有关闭了该界面才能对其他界面进行操作
		#若使用show()的话，那注册界面就是非模态的，
		#则在显示了注册界面后，还能同时对登录界面进行操作(QDialog有exec_()方法

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

if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo=Demo()
	demo.show()
	sys.exit(app.exec_())

####1.setPlaceholderText()方法用于在输入框显示浅灰色的提示文本；
####2.exec_()方法可以让窗口成为模态窗口，而调用show()方法，窗口是非模态的。
####模态窗口将程序控制权占据，只有对当前窗口关闭后才能操作其他窗口；
####3.QDialog有exec_()方法，而QWidget没有；
###4.可以用setEchoMode(QLineEdit.Password)将普通输入框中的文字变成原点。