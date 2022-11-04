# -*- coding: utf-8 -*-
import sys
from PySide.QtGui   import QApplication,QLabel

if __name__ == '__main__':
	app = QApplication(sys.argv)#1例化一个QApplication，并将sys.argv作为参数传入
	label = QLabel()#2实例化一个QLabel控件
	label.setText("Hello World!")
	label.show()# 通过调用show()方法使控件可见
	sys.exit(app.exec_())#app.exec_()是执行应用，让应用开始运转循环，直到窗口关闭返回0给sys.exit()，退出整个程序。