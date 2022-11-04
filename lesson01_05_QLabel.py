# -*- coding: utf-8 -*-
import sys
from PySide.QtCore import Signal
from PySide.QtGui import QApplication,QWidget,QLabel

class Demo(QWidget):
	my_signal = Signal()

	"""docstring for Demo"""
	def __init__(self):
		super(Demo, self).__init__()
		self.label = QLabel('Hello World', self)
		self.my_signal.connect(self.change_text)
	def change_text(self):
		if self.label.text() == 'Hello World':
			self.label.setText('Hello PyQt')
		else:
			self.label.setText('Hello World')

	def mousePressEvent(self, event):                     # 4
		self.my_signal.emit()  

if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Demo()
	demo.show()
	sys.exit(app.exec_())