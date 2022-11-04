# -*- coding: utf-8 -*-
import sys
from PySide.QtGui   import QApplication,QWidget,QPushButton

class Demo(QWidget):#该类继承QWidget
	"""docstring for ClassName"""
	def __init__(self,):
		super(Demo, self).__init__()
		self.button = QPushButton('Start',self)#实例化一个QPushButton
		self.button.clicked.connect(self.change_text)#连接信号与槽函数

	def change_text(self):
		print('change_text')
		self.button.setText('Stop')#将按钮文本从‘Start’改成‘Stop’
		self.button.clicked.disconnect(self.change_text)#信号和槽解绑

if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo=Demo()#实例化Demo类
	demo.show()#使demo可见
	sys.exit(app.exec_())

