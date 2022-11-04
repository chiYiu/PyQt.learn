# -*- coding: utf-8 -*-
#QScrollArea和QScrollBar的基本用法
#滚动区域QScrollArea
# 滚动条QScrollBar
#Zoom in按钮和Zoom out按钮分别用于放大缩小图片

import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication,QWidget,QPushButton,QLabel,QScrollArea,\
						QScrollBar,QHBoxLayout,QVBoxLayout,QPixmap

class Demo(QWidget):
	"""docstring for Demo"""
	def __init__(self):
		super(Demo, self).__init__()
		self.label = QLabel(self)
		#实例化一个QLabel控件用于显示大图
		self.label.setPixmap(QPixmap('images/image.jpg'))
		self.label.setScaledContents(True)
		#setScaledContents(True)方法可以让图片随着QLabel控件大小变化而变化，即自适应

		self.scroll_area = QScrollArea(self)
		#实例化一个QScrollArea控件
		self.scroll_area.setWidget(self.label)
		#用setWidget()方法可将QLabel设置为滚动区域的控件
		self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		#这行代码将滚动区域自导的横向动条给隐藏，因为我们要用自己的滚动条

		self.scrollbar = QScrollBar(Qt.Horizontal,self)
		#实例化一个横向滚动条
		self.scrollbar.setMaximum(self.scroll_area.horizontalScrollBar().maximum())
		#调用setMaximum()方法设置最大值。而它的最大值应该跟QScrollArea被隐藏掉的横向滚动条的最大值一样

		self.bigger_btn = QPushButton('Zoom in',self)
		self.smaller_btn = QPushButton('Zoom out',self)
		#实例化两个按钮用于放大缩小QLabel控件(图片也会相应的放大缩小)

		self.bigger_btn.clicked.connect(self.bigger_func)
		 #信号和槽函数连接bigger_func()槽函数
		self.smaller_btn.clicked.connect(self.smaller_func)
		#信号和槽函数连接smaller_func()槽函数
		self.scrollbar.valueChanged.connect(self.sysnc_func)
		#信号和槽函数连接sysnc_func()槽函数

		self.h_layout = QHBoxLayout()
		self.h_layout.addWidget(self.bigger_btn)
		self.h_layout.addWidget(self.smaller_btn)

		self.v_layout = QVBoxLayout()
		self.v_layout.addWidget(self.scroll_area)
		self.v_layout.addWidget(self.scrollbar)
		self.v_layout.addLayout(self.h_layout)
		self.setLayout(self.v_layout)
	
	def bigger_func(self):
		self.label.resize(self.label.width()*1.2,self.label.height()*1.2)
		self.scrollbar.setMaximum(self.scroll_area.horizontalScrollBar().maximum())
		#我们将QLabel控件放大20%，同时设置QScrollBar的最大值为QScrollArea横向滚动条的最大值

	def smaller_func(self):
		self.label.resize(self.label.width()*0.8,self.label.height()*0.8)
		self.scrollbar.setMaximum(self.scroll_area.horizontalScrollBar().maximum())
		#将QLabel控件缩小20%，同样要更新QScrollBar的最大值

	def sysnc_func(self):
		self.scroll_area.horizontalScrollBar().setValue(self.scrollbar.value())
		#我们让QScrollArea横向滚动条的当前值和QScrollBar的值同步。
		#这样一来就相当于我们在用自己实例化的QScrollBar来控制滚动区域中的图片

if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Demo()
	demo.show()
	sys.exit(app.exec_())