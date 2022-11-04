# -*- coding: utf-8 -*-
#要实现多线程，我们要先继承QThread类并重新实现其中的run()函数，
#也就是说把耗时的操作放入run()函数中。
#比如我们把上面例子的计数操作放在run()函数中

import sys
import time
import urllib2#python2
from PySide.QtCore import Qt,QThread,Signal
from PySide.QtGui import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QHBoxLayout

class Demo(QWidget):
	def __init__(self):
		super(Demo,self).__init__()
		self.count = 0

		self.button = QPushButton(u'开始',self)
		self.button.clicked.connect(self.start_func)

		self.label = QLabel(u'准备开始',self)
		self.label.setAlignment(Qt.AlignCenter)

		self.crawl_thread = CrawlThread()
		self.crawl_thread.status_signal.connect(self.status_func)
		#在UI线程中进行信号和槽的连接

		self.v_layout = QVBoxLayout()
		self.v_layout.addWidget(self.label)
		self.v_layout.addWidget(self.button)
		self.setLayout(self.v_layout)

	def start_func(self):
		self.crawl_thread.start()

	def status_func(self,status):
		self.label.setText(status)
	#在槽函数中我们将label的值设为传递过来的数值

class CrawlThread(QThread):
	status_signal = Signal(str)
	#首先在MyThread()类中自定义一个信号，Signal(str)加上str就代表这个信号可以传一个字符串数值

	def __init__(self):
		super(CrawlThread,self).__init__()

	def run(self):
		self.status_signal.emit(u'爬虫工作中')
		response = urllib2.urlopen("https://www.yutu.cn/")
		self.status_signal.emit(u'保存')
		with open('python.txt','w') as f:
			f.write(response.read())
			self.status_signal.emit(u'完成')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())