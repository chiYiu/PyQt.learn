# -*- coding: utf-8 -*-
####表格控件QTableWidget####
import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication,QTableWidget,QTableWidgetItem

class Demo(QTableWidget):
	"""docstring for Demo"""
	def __init__(self):
		super(Demo, self).__init__()
		self.resize(600,250)
		self.setRowCount(6)
		#setRowCount(int)设置表格的行数
		self.setColumnCount(6)
		#setColumnCount(int)设置列数
		#self.table = QTableWidget(6,6,self)
		#或者可以选择在实例化的时候直接指定行列数

		print(self.rowCount())
		#rowCount()获取行数
		print(self.columnCount())
		#columnCount()获取列数

		self.setColumnWidth(0,50)
		self.setRowHeight(0,30)
		#setColumnWidth(int, int)设置列款，第一个参数填列序号，第二个参数填宽度值。
		#setRowCount(int, int)设置行宽，参数同理

		self.setHorizontalHeaderLabels(['h0','h1','h2','h3','h4','h5'])
		#setHorizontalHeaderLabels(iterable)设置行的标题
		self.setVerticalHeaderLabels(['t0','t1','t2','t3','t4','t5'])
		#setVerticalHeaderLabels设置列的标题

		#self.setShowGrid(False)
		#setShowGird(bool)设置是否显示表格上的网格线

		self.item_1 = QTableWidgetItem('Hi')
		self.setItem(0,0,self.item_1)
		#实例化一个单元格，并用setItem(int, int, QTableWidgetItem)将该单元格添加到表格中
		#前两个int类型参数分别为行序号和列序号
		self.item_2 = QTableWidgetItem('Bye')
		self.item_2.setTextAlignment(Qt.AlignCenter)
		#setTextAlignment()设置单元格的文本对齐方式
		self.setItem(2,2,self.item_2)

		self.setSpan(2,2,2,2)
		#setSpan(int, int, int, int)方法用来合并单元格，前两个int参数分别为行序号和列序号
		#后两个分别为要合并的行数和列数

		print(self.findItems('Hi',Qt.MatchExactly))
		print(self.findItems('B',Qt.MatchContains))
		# findItems(str, Qt.MatchFlag)方法用来进行查找
		#Qt.MatchExactly表示精确匹配
		#Qt.MatchContains表示包含匹配

if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Demo()
	demo.show()
	sys.exit(app.exec_())