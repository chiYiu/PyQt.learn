# -*- coding: utf-8 -*-
#当在执行某些复杂且耗时的操作时，我们不能将该操作放在界面控制线程中(即UI线程，就是app.exec_()所在的线程)，
#否则我们会发现界面停止响应(或卡顿)，比如下面这个例子就是

import sys
import time
from PySide.QtCore import Qt
from PySide.QtGui import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout

class Demo(QWidget):
	def __init__(self):
		super(Demo,self).__init__()
		self.count = 0

		self.button = QPushButton('Count',self)
		self.button.clicked.connect(self.count_func)
		self.label = QLabel('0',self)
		self.label.setAlignment(Qt.AlignCenter)

		self.v_layout = QVBoxLayout()
		self.v_layout.addWidget(self.label)
		self.v_layout.addWidget(self.button)
		self.setLayout(self.v_layout)

	def count_func(self):
		while True:
			self.count +=1
			self.label.setText(str(self.count))
			time.sleep(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

#为解决这种情况，我们应该采用多线程，将复杂耗时的操作放在与界面控制不同的线程中，
#让两者独立开来。下面我们就来了解下如何使用多线程(第十章中讲到的QTimer也属于多线程技术，
#所以同样可以解决上述程序中的界面卡死问题