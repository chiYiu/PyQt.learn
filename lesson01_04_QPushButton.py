# -*- coding: utf-8 -*-
import sys
from PySide.QtGui import QApplication,QWidget,QPushButton

class Demo(QWidget):
	"""docstring for Demo"""
	def __init__(self):
		super(Demo, self).__init__()
		self.resize(300,300)
		self.setWindowTitle('demo')
		self.button = QPushButton('Start',self)
		self.button.clicked.connect(self.change_text)
		self.button.clicked.connect(self.change_window_size)
		self.button.clicked.connect(self.change_window_title)

	def change_text(self):
		print('change text')
		self.button.setText('Stop')
		self.button.clicked.disconnect(self.change_text)

	def change_window_size(self):
		print('change window size')
		self.resize(500,500)
		self.button.clicked.disconnect(self.change_window_size)

	def change_window_title(self):
		print('change_window_title')
		self.setWindowTitle('window title changed')
		self.button.clicked.disconnect(self.change_window_title)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Demo()
	demo.show()
	sys.exit(app.exec_())