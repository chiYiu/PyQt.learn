# -*- coding: utf-8 -*-
#窗口QSplitter、标签页窗口QTabWidget、堆叠窗口QStackedWidget、停靠窗口QDockWidget以及多文档界面QMidiArea
#这些类可以帮助我们加入更多的控件，更多的功能，而且不会让界面看起来混乱


###拆分窗口QSplitter###
import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication,QSplitter,QListView,QTreeView,QTableView,QDirModel
		
class Demo(QSplitter):
    #继承QSplitter
	def __init__(self):
		super(Demo, self).__init__()
		self.dir_model = QDirModel(self)
		#实例化QDirModel模型

		self.list_view = QListView(self)
		self.tree_view = QTreeView(self)
		self.table_view = QTableView(self)
		self.list_view.setModel(self.dir_model)
		self.tree_view.setModel(self.dir_model)
		self.table_view.setModel(self.dir_model)
		#分别实例化QListView、QTreeView和QTableView，然后将这三个视图的模型设为dir_model

		self.tree_view.doubleClicked.connect(self.show_func)
		#将QTreeView的doubleClicked信号和自定义的槽函数连接起来

		#self.setOrientation(Qt.Vertical)
		#可以调用setOrientation(Qt.Vertical)方法将其设为垂直方向
		self.addWidget(self.list_view)
		self.addWidget(self.tree_view)
		#调用addWidget()方法将视图添加到拆分窗口中
		self.insertWidget(0,self.table_view)
		#insrtWidget(int, widget)可以将控件插入到相应的位置，第一个参数为要插入的索引位置，第二个参数为控件
		
		self.setSizes([300,200,200])
		#setSizes(iterable)可以设置各个子控件的宽度
		print(self.count())


	def show_func(self,index):
		self.list_view.setRootIndex(index)
		self.table_view.setRootIndex(index)
		#调用setRootIndex()并传入index值，也就是说，每当我们双击QTreeView中的某项时
		#QListView和QTableView就会将该项的索引设为自身的根索引，并显示相应的目录结构
		
		

if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Demo()
	demo.show()
	sys.exit(app.exec_())