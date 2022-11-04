# -*- coding: utf-8 -*-
#选择器不单单有上面那种写法，一下总结了几种写法：
#选择器类型   例子     					解释
#通用选择器   *        					匹配所以控件
#类型选择器   QPushButton    			匹配所有QPushButton实例及其子类
#属性选择器   QPushButton[name='btn']	匹配所有name属性为btn的QPushButton实例
#			 QPushButton[name~='btn]	~代表匹配所有name属性中包含btn的QPushButton实例
#类选择器 	 .QPushButton               匹配所有QPushButton实例，但不匹配其子类，等同于*[class~='QPushButton']
#ID选择器	 QPushButton#okButton 		匹配所有objectName为okButton的QPushButton实例
#后代选择器	 QDialog QPushButton        匹配所有QDialog控件中包含的QPushButton实例(无论直接还是间接包含)
#子选择器	 QDialog>QPushButton 		匹配所有QDialog控件中直接包含的QPushButton实例

#*{color:red}# 所有控件设置为红色
#QPushButton{background-color:blue}#把所有QPushButton实例及其子类的背景颜色设置为蓝色
#QPushButton[name='btn']{background-color:green}#把所有name属性为btn的QPushButton实例的背景颜色设为绿色
#.QLineEdit{font: bold 20px}#把所有QLineEdit实例(不包括子类)的字体变粗，大小设置为20px
#QComboBox#cb {color:blue}#把所有objecName为cb的下拉框文本设置为蓝色
#QGroupBox QLabel{color:blue}#把所有包含在QStackedWidget中的QLabel控件的文本颜色设置为蓝色
#QGroupBox>QLabel {font: 30px}#把所有QStackedWidget直接包含的QLabel文本字体大小设置为30px

import sys
from PySide.QtGui import QApplication,QWidget,QPushButton,QLabel,QLineEdit,QVBoxLayout,QHBoxLayout,\
							QComboBox,QStackedWidget,QGroupBox

class Demo(QWidget):
	def __init__(self):
		super(Demo,self).__init__()
		self.button1 = QPushButton('button1',self)#实例化QPushButton
		self.button2 = QPushButton('button2',self)#实例化QPushButton
		self.button2.setProperty('name','btn')#给button2添加name属性

		self.lineedit1 = QLineEdit(self)#实例化一个QLineEdit
		self.lineedit1.setPlaceholderText('direct')#设置占位符文本
		self.lineedit2 = SubLineEdit()#实例化一个自定义QLineEdit类

		my_list = ['A','B','C','D']
		self.combo = QComboBox(self)#实例化一个QComboBox控件
		self.combo.addItems(my_list)
		self.combo.setObjectName('cb')#调用setObjectName()方法将其objectName设置为cb

		self.gb = QGroupBox()#实例化一个QGroupBox控件
		self.label1 = QLabel('label1')#实例化一个QLabel
		self.label2 = QLabel('label2')#实例化一个QLabel
		self.stack = QStackedWidget()#实例化一个QStackedWidget控件
		#添加self.label2到self.stack控件
		self.stack.addWidget(self.label2)

		#实例化一个QVBoxLayout布局
		self.gb_layout = QVBoxLayout()
		#添加self.label1到self.gb_layout
		self.gb_layout.addWidget(self.label1)
		#添加self.stack到self.gb_layout
		self.gb_layout.addWidget(self.stack)
		self.gb.setLayout(self.gb_layout)

		#实例化布局QVBoxLayout，并添加控件
		self.v_layout = QVBoxLayout()
		self.v_layout.addWidget(self.button1)
		self.v_layout.addWidget(self.button2)
		self.v_layout.addWidget(self.lineedit1)
		self.v_layout.addWidget(self.lineedit2)
		self.v_layout.addWidget(self.combo)
		self.v_layout.addWidget(self.gb)
		self.setLayout(self.v_layout)

class SubLineEdit(QLineEdit):
	def __init__(self):
		super(SubLineEdit,self).__init__()
		self.setPlaceholderText('indirect')
		#自定义一个QLineEdit子类

if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Demo()
	qss = '''
		 *{color:red}
		 QPushButton {background-color: blue}
		 QPushButton[name='btn'] {background-color: green}
		 .QLineEdit {font: bold 20px}
		 QComboBox#cb {color: blue}
		 QGroupBox QLabel {color: blue}
		 QGroupBox>QLabel {font: 30px}
		  '''
	demo.setStyleSheet(qss)
	demo.show()
	sys.exit(app.exec_())