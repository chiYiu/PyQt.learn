# -*- coding: utf-8 -*-
#每条QSS样式都由两部分组成:1.选择器2. 声明
#QPushButton {color: red}

import sys
from PySide.QtGui import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QHBoxLayout

class Demo(QWidget):
	def __init__(self):
		super(Demo,self).__init__()
		self.button1 = QPushButton('super class', self)
		self.button2 = SubButton()

		self.h_layout = QHBoxLayout()
		self.h_layout.addWidget(self.button1)
		self.h_layout.addWidget(self.button2)
		self.setLayout(self.h_layout)

class SubButton(QPushButton):
	def __init__(self):
		super(SubButton, self).__init__()
		self.setText('subclass')

if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Demo()
	qss = 'QPushButton {color: red}'
	demo.setStyleSheet(qss)
	demo.show()
	sys.exit(app.exec_())