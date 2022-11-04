# -*- coding: utf-8 -*-
import sys
from PySide.QtGui import QIcon,QApplication,QWidget,QPushButton

#QPushButton
class Demo(QWidget):
	"""docstring for Demo"""
	def __init__(self):
		super(Demo, self).__init__()
		self.test_button = QPushButton('Test',self)
		self.test_button.setCheckable(True) #按钮有标记和非标记两种状态,设置为可标记的按钮
		self.test_button.setIcon(QIcon('cancel.png'))#通过setIcon()方法给按钮设置一个图标，传入的参数为QIcon()
		self.test_button.toggled.connect(self.button_state_func)

	def button_state_func(self):
		print(self.test_button.isChecked())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec_())
#toggled信号是专门用来配合按钮标记状态变化的，
#也就是说按钮标记状态发生变化就会发出toggled信号。
#在这里将toggled信号和自定义的槽函数连接了起来；
#通过isChecked()方法来判断按钮是否为标记状态，若是则返回True，不是则返回False
