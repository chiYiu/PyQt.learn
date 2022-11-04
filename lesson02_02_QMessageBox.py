# -*- coding: utf-8 -*-
import sys
from PySide.QtGui   import QApplication,QWidget,QPushButton,QMessageBox

class Demo(QWidget):
	"""docstring for Demo"""
	def __init__(self):
		super(Demo, self).__init__()
		self.button = QPushButton('Click Me!',self)
		self.button.clicked.connect(self.show_messagebox)

	def show_messagebox(self):
		choice = QMessageBox.question(self, 'Change Text?', 'Would you like to change the button text?',
				QMessageBox.Yes | QMessageBox.No)  # 1

		if choice == QMessageBox.Yes:# 2
			self.button.setText('Changed!')
		elif choice == QMessageBox.No:# 4
			pass
		#msgBox = QMessageBox()
		#connectButton = msgBox.addButton(self.tr("Connect"), QMessageBox.ActionRole)
		#abortButton = msgBox.addButton(QMessageBox.Abort)
		#msgBox.exec_()
		#if msgBox.clickedButton() == connectButton:
		#	print "a"
		#elif msgBox.clickedButton() == abortButton:
		#	print "b"
if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Demo()
	demo.show()
	sys.exit(app.exec_())