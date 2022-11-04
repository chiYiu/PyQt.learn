# -*- coding: utf-8 -*-
####列表视图、树形视图、表格视图####


##树形视图QTreeView###

import sys
from PySide.QtCore import Qt,QDir
from PySide.QtGui import QApplication,QWidget,QTreeView,QLabel,QVBoxLayout,\
						QDirModel

class Demo(QWidget):
	"""docstring for Demo"""
	def __init__(self):
		super(Demo, self).__init__()
		self.resize(600,300)
		self.model = QDirModel(self)
		#实例化一个QDirModel模型
		self.model.setReadOnly(False)
		#setReadOnly(False)方法可以让我们在QTreeView中直接对文件进行编辑
		self.model.setSorting(QDir.Name | QDir.IgnoreCase)
		#setSorting()方法可以让显示的文件或文件夹按照指定要求进行排序

		self.tree = QTreeView(self)
		#实例化一个树形视图
		self.tree.setModel(self.model)
		#将其模型设为self.model
		self.tree.clicked.connect(self.show_info)
		#将clicked信号和自定义的槽函数连接起来
		self.index = self.model.index(QDir.currentPath())
		#通过调用self.model的index()方法传入一个QDir.currentPath()来获取当前路径的QModelIndex索引值

		self.tree.expand(self.index)
		#调用self.tree的expand()方法进行展开显示
		self.tree.scrollTo(self.index)
		#scrollTo()方法则是将当前视图的视口滚动到self.index索引处

		self.info_label = QLabel(self)
		#info_label用于显示文件信息


		self.v_layout = QVBoxLayout()
		self.v_layout.addWidget(self.tree)
		self.v_layout.addWidget(self.info_label)
		self.setLayout(self.v_layout)

	def show_info(self):
		index = self.tree.currentIndex()
		file_name = self.model.fileName(index)
		file_path = self.model.filePath(index)
		file_info = u'File name:{}\nFile Path:{}'.format(file_name,file_path)
		self.info_label.setText(file_info)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Demo()
	demo.show()
	sys.exit(app.exec_())