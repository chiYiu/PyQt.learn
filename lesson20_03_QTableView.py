# -*- coding: utf-8 -*-
####列表视图、树形视图、表格视图####


##表格视图QTableView###

import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication,QWidget,QTableView,QLabel,QVBoxLayout,\
						QAbstractItemView,QStandardItem,QStandardItemModel

class Demo(QWidget):
	"""docstring for Demo"""
	def __init__(self):
		super(Demo, self).__init__()
		self.resize(650,300)

		self.model = QStandardItemModel(6,6,self)
		#实例化一个QStandItemMode
		#self.model = QStandardItemModel(self)
		#self.model.setColumnCount(6)
		#self.model.setRowCount(6)
		#也可以通过setRowCount()和setColumn()方法来设置


		for row in range(6):
			for column in range(6):
				item = QStandardItem('({},{})'.format(row,column))
				self.model.setItem(row,column,item)
		#QStandItemModel与QStandardItem搭配使用，
		#这里通过循环实例化36个QStandardItem(每一个item代表一个单元格)，
		#接着调用setItem()方法将每一个Item放在相应的位置


		self.item_list = [QStandardItem('(6,{})'.format(column)) for column in range(6)]
		self.model.appendRow(self.item_list)
		#appendRow()方法可以把新行添加到表格最后，也就是说目前有7行

		self.item_list = [QStandardItem('(7,{})'.format(column)) for column in range(6)]
		self.model.insertRow(7,self.item_list)
		# insertRow()方法可以在指定方法添加一行，这里我们在最后一行插入一行，现在有8行；

		self.tabel = QTableView(self)
		# 实例化一个QTableView
		self.tabel.setModel(self.model)
		#设置模型
		self.tabel.horizontalHeader().setStretchLastSection(True)
		#self.table.horizontalHeader().setStretchLastSection(True)可以让表格填满整个窗口
		#如果拉伸窗口的话则为了填满窗口表格最后列会改变尺寸
		self.tabel.setEditTriggers(QAbstractItemView.NoEditTriggers)
		#setEditTriggers()方法设置编辑规则，这里我们设置无法编辑。
		self.tabel.clicked.connect(self.show_info)
		#最后将clicked信号和自定义的槽函数连接起来

		self.info_label = QLabel(self)
		#info_label用于显示单元格文本
		self.info_label.setAlignment(Qt.AlignCenter)
		#居中
		
		self.v_layout = QVBoxLayout()
		self.v_layout.addWidget(self.tabel)
		self.v_layout.addWidget(self.info_label)
		self.setLayout(self.v_layout)


	def show_info(self):
		row = self.tabel.currentIndex().row()
		column = self.tabel.currentIndex().column()
		print('{},{}'.format(row,column))

		data = self.tabel.currentIndex().data()
		self.info_label.setText(data)
	#currentIndex().row()可以获取当前点击单元格所在的行序号，
	#currentIndex().column()可以获取当前点击单元格所在的列序号。
	#currentIndex().data()可以获取到当前点击单元格的文本

if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Demo()
	demo.show()
	sys.exit(app.exec_())