# -*- coding: utf-8 -*-
####列表控件QListWidget####
import sys
from PySide.QtGui import QApplication,QPixmap,QWidget,QLabel,QListWidget,QListWidgetItem,QHBoxLayout

class Demo(QWidget):
	"""docstring for Demo"""
	def __init__(self):
		super(Demo, self).__init__()
		self.pic_label = QLabel(self)
		self.pic_label.setPixmap(QPixmap('images/arrow.png'))
		#pic-label用来显示图片

		self.listwidget_1 = QListWidget(self)
		#实例化QListWidget
		self.listwidget_2 = QListWidget(self)
		#实例化QListWidget
		self.listwidget_1.doubleClicked.connect(lambda:self.change_func(self.listwidget_1))
		#连接QListWidget控件得doubleClicked信号和自定义函数槽连接起来
		self.listwidget_2.doubleClicked.connect(lambda:self.change_func(self.listwidget_2))
		#连接QListWidget控件得doubleClicked信号和自定义函数槽连接起来

		for i in range(6):
			text = 'Item {}'.format(i)
			self.item = QListWidgetItem(text)
			self.listwidget_1.addItem(self.item)
		#创建6个QListWidgetItem,并通过调用addItem(QListWidgetItem)添加到listwidget_1中

		self.item_6 = QListWidgetItem('item 6',self.listwidget_1)
		#通过实例化时指定父类得方式添加

		self.listwidget_1.addItem('item 7')
		#直接调用addItem(str)方法来添加一项内容
		str_list = ['item 9', 'item 10']
		self.listwidget_1.addItems(str_list)
		#通过addItems(labels)来添加项目组

		self.item_8 = QListWidgetItem('item 8')
		self.listwidget_1.insertItem(8,self.item_8)
		#通过insetItem(row,QListWidgetItem)方法指定行加入内容

		self.h_layout = QHBoxLayout()
		self.h_layout.addWidget(self.listwidget_1)
		self.h_layout.addWidget(self.pic_label)
		self.h_layout.addWidget(self.listwidget_2)
		self.setLayout(self.h_layout)
		##指定布局

	def change_func(self,listwidget):
		if listwidget == self.listwidget_1:
			#判断信号是哪个QListWidget发出的，如果是listwidget_1
			item = QListWidgetItem(self.listwidget_1.currentItem())
			#通过currentItem()获取到当前被双击的项，然后实例化QListWidgetItem
			self.listwidget_2.addItem(item)
			#通过addItem(QListWidgetItem)加入listwidget_2中
			print(self.listwidget_2.count())
			#count()获取项数量并打印项数量
		else:
			self.listwidget_2.takeItem(self.listwidget_2.currentRow())
			#如果信号是listwidget_2发出，双击项的行数传给takeItem(int)方法来进行删除
			print(self.listwidget_2.count())
			#count()获取项数量并打印项数量

if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Demo()
	demo.show()
	sys.exit(app.exec_())