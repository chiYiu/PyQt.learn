# -*- coding: utf-8 -*-
#伪状态选择器可以让我们针对某控件的不同状态进行QSS样式化操作，
#下面我们以QPushButton和QComboBox为例

import sys
from PySide.QtGui import QApplication,QWidget, QPushButton, QComboBox, QVBoxLayout

class Demo(QWidget):
	def __init__(self):
		super(Demo,self).__init__()
		self.button1 = QPushButton('button1', self)
		self.button2 = QPushButton('button2', self)
		self.button2.setProperty('name', 'btn2')

		my_list = ['A', 'B', 'C', 'D']
		self.combo = QComboBox(self)
		self.combo.addItems(my_list)

		self.v_layout = QVBoxLayout()
		self.v_layout.addWidget(self.button1)
		self.v_layout.addWidget(self.button2)
		self.v_layout.addWidget(self.combo)
		self.setLayout(self.v_layout)



if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Demo()
	qss = '''
		  QPushButton:hover {background: red}
		  QPushButton[name='btn2']:pressed {background: blue}
		  QComboBox::drop-down:hover {background: green}
		  '''
		  ##伪状态选择器写法就是在控件名后加一个英文状态下的冒号:再加上伪状态即可
		  
		  #当鼠标悬停在QPushButton实例或其子类上时，将背景变为红色 
		  #当鼠标在QPushButton实例或其子类上按下时，将背景变为蓝色(但只针对name属性为btn2的QPushButton实例及子类)
		  #当鼠标在QComboBox实例或其子类的下拉按钮子控件上悬停时，将下拉按钮的背景色改为绿色
	demo.setStyleSheet(qss)
	demo.show()
	sys.exit(app.exec_())