# -*- coding: utf-8 -*-
import sys
from PySide.QtGui import QIcon,QApplication,QWidget,QToolButton

#QToolButton是与工具操作相关的按钮
class Demo(QWidget):
	"""docstring for Demo"""
	def __init__(self):
		super(Demo, self).__init__()
		self.test_button = QToolButton(self)
		self.test_button.setCheckable(True)
		self.test_button.setIcon(QIcon('cancel.png'))
		self.test_button.toggled.connect(self.button_state_func)
		self.test_button.isChecked()

	def button_state_func(self):
		print(self.test_button.isChecked())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec_())

#请注意不能在QToolButton实例化的时候直接传入文本字符串，
#因为该控件没有相应的初始化函数。
#也就是说这样做是错误的：self.test_button = QToolButton('Test', self)
# 如果要设置文本的话得通过setText()方法。
#但是setText()方法和setIcon()方法都使用的话，只会显示图标