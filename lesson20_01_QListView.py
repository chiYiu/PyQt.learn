# -*- coding: utf-8 -*-
####列表视图、树形视图、表格视图####
#在前一张所讲的列表控件QListWidget，树形控件QTreeWidget和表格控件QTableWidget是基于项(item-based)的控件
#它们分别与QListWidgetItem，QTreeWidgetItem以及QTableWidgetItem一起使用。
#在基于项的控件中，数据是存储于项中再由对应的控件添加进去并显示的。而我们这章所讲的列表视图QListView
#树形视图QTreeView和表格视图QTableView是基于模型的(model-based)，
#也就是说有关数据的获取或者存储操作都是跟模型有关。当我们在处理大量数据的时候，
#采用基于模型的控件可以让程序的处理速度更快，性能更好
#QListView，QTreeView和QTableView分别是QListWidget，QTreeWidget和QTableWidget的父类，
#后三者的目的主要是为了使用方便，让开发更加快速(不过还是习惯将前三者称作视图，后三者称为控件，比较好区分)。
#在高端复杂的程序中，还是建议使用前三者

#模型种类及用处
#QStringListModel 			储存一个字符串列表
#QStandardItemModel			储存任意的分层的数据
#QDirModel 					封装本地文件系统
#QSqlQueryModel 			封装一个SQL结果集
#QSqlTableModel 		 	封装一个SQL表
#QSqlRelationalTableModel 	利用外键封装一个SQL表
#QSortFilterProxyModel		对模型数据进行排序或过滤

##列表视图QListView###

import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication,QPixmap,QWidget,QListView,QLabel,QHBoxLayout,\
						QAbstractItemView,QStringListModel

class Demo(QWidget):
	"""docstring for Demo"""
	def __init__(self):
		super(Demo, self).__init__()
		
		self.item_list = ['item %s' %i for i in range(11)]
		#用列表推导式生成11个item
		self.model_1 = QStringListModel(self)
		#例化一个QStringListModel
		self.model_1.setStringList(self.item_list)
		#setStringList(iterable)方法将数据添加到到模型中
		self.model_2 = QStringListModel(self)
		#model_1用于listview_1，model_2用于listview_2

		self.listView_1 = QListView(self)
		#实例化一个列表视图listview_1
		self.listView_1.setModel(self.model_1)
		#调用setModel(model)方法将model_1作为参数传入
		#此时，列表视图就会显示出模型中的数据，模型数据发生任何改变，视图也会自动作出相应改变
		self.listView_1.setEditTriggers(QAbstractItemView.NoEditTriggers)
		#setEditTriggers()方法可设置视图的编辑规则,可传入的参数如下
		#QAbstractItemView.NoEditTriggers 无法编辑
		#QAbstractItemView.CurrentChanged 当选择项发生改变时可编辑
		#QAbstractItemView.DoubleClicked  双击时可编辑
		#QAbstractItemView.EditKeyPressed 按下编辑键时可编辑
		self.listView_1.doubleClicked.connect(lambda:self.change_func(self.listView_1))
		#将视图的doubleClicked信号与自定义的槽函数change_func()连接了起来

		self.listView_2 = QListView(self)
		self.listView_2.setModel(self.model_2)
		self.listView_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.listView_2.doubleClicked.connect(lambda:self.change_func(self.listView_2))

		self.pic_label = QLabel(self)
		self.pic_label.setPixmap(QPixmap('images/arrow.png'))

		self.h_layout = QHBoxLayout()
		self.h_layout.addWidget(self.listView_1)
		self.h_layout.addWidget(self.pic_label)		self.h_layout.addWidget(self.listView_2)
		self.setLayout(self.h_layout)
		

	def change_func(self,listView):
		if listView == self.listView_1:
			#在槽函数中我们判断触发doubleClicked信号的视图
			self.model_2.insertRows(self.model_2.rowCount(),1)
			#通过insertRows(int, int)方法先在model_2中插入一个空行，该方法的第一个参数为行序号
			#第二个为要插入的行数量，。在这里rowCount()方法获取总行数
			#在这里正好可以当做行序号，表示我们将新行添加到最后一行，1表示我们在每次双击时都只插入一行

			data = self.listView_1.currentIndex().data()
			#currentIndex().data()方法可以获取到被双击行的数据
			#比如双击在'Item 0'上，那么我们就获取了‘Item 0’这个文本

			index = self.model_2.index(self.model_2.rowCount()-1)
			#QStringListModel的index(int)方法获取到指定的QModelIndex，传入的参数为行序号(请注意序号都是从0开始计算)
			self.model_2.setData(index,data)
			##由于插入的只是空行，所以我们要调用setData(QModelindex, data)方法将该空行设为相应的内容
		else:
			self.model_2.removeRows(self.listView_2.currentIndex().row(),1)
			#如果是listview_2触发doubleClicked信号的话，那我们就通过调用removeRows(int, int)，方法将被双击的行给删除掉。
			#currentIndex().row()方法获取被双击行的行序号，1表示我们只删除一行
if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Demo()
	demo.show()
	sys.exit(app.exec_())