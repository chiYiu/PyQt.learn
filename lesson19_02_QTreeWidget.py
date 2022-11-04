# -*- coding: utf-8 -*-
####树形控件QTreeWidget####
import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication,QPixmap,QWidget,QTreeWidget,QTreeWidgetItem,QLabel,QHBoxLayout

class Demo(QWidget):
	"""docstring for Demo"""
	def __init__(self):
		super(Demo, self).__init__()
		self.resize(500,300)
		self.label = QLabel('No Click')
		#用于显示每个QtreeWidgetItem的文本

		self.tree = QTreeWidget(self)
		#实例化一个QTreeWidget
		self.tree.setColumnCount(2)
		#通过setColumnCount(int)将该树状控件的列数设为2
		self.tree.setColumnWidth(0,300)
		#setColumnWidth(Column,width)将该树状控件的宽度
		self.tree.setHeaderLabels(['Install Component','Test'])
		#设置每列的标题，如果有一列的话应该通过setHeaderLabel(str)方法
		self.tree.itemClicked.connect(self.change_func)
		#连接itemClicked信号与自定义函数槽，每当点击QTreeWidget的任意一项，都会触发itemClicked信号
		#这是一个带参数的信号，当信号触发，参数item保存被点击的项，colunm保存列数，
		#而这两个参数自动传递给我们的槽函数，我们的槽函数也带了两个参数

		self.preview = QTreeWidgetItem(self.tree)
		#实例化一个QTreeWidgetItem，设置父类为self.tree，表示self.preview为顶层的项
		self.preview.setText(0, 'Preview')
		#设置文本setText(int,str) int为列，0表示第一列
		#self.preview = QTreeWidgetItem()
		#self.preview.setText(0, 'Preview')
		#self.tree.addTopLevelItem(self.preview)
		#我们可以不指定父类，并让self.tree调用addTopLevelItem()方法来设置最顶层的项

		self.qt5112 = QTreeWidgetItem()
		#实例化项
		self.qt5112.setText(0,'Qt 5.11.2 snapshot')
		#设置项label
		self.qt5112.setCheckState(0,Qt.Unchecked)
		#setCheckState(int, CheckState)方法可以让该项以复选框形式呈现出来
		self.preview.addChild(self.qt5112)
		#addChild(QTreeWidgetItem)方法可以添加子项，让self.preview添加一个self.qt5112选项
		choice_list = ['macOS', 'Android x86', 'Android ARMv7','Sources','iOS']
		self.item_list = []
		for i,c in enumerate(choice_list):
			item = QTreeWidgetItem(self.qt5112)
			item.setText(0,c)
			item.setCheckState(0,Qt.Unchecked)
			self.item_list.append(item)
		#实例化5个子项，将他们添加到self.qt5112中，并以复选框形式显示

		self.test_item = QTreeWidgetItem(self.qt5112)
		self.test_item.setText(0, 'test1')
		self.test_item.setText(1, 'test2')
		#这里的self.test项只是拿来作为对比QTreeWidget设为两列时的样子
		self.tree.expandAll()

		self.h_layout = QHBoxLayout()
		self.h_layout.addWidget(self.tree)
		self.h_layout.addWidget(self.label)
		self.setLayout(self.h_layout)

	def change_func(self,item,column):
		self.label.setText(item.text(column))

		print(item.text(column))
		print(column)
		if item.text(column) == self.qt5112.text(column):
			if self.qt5112.checkState(0) == Qt.Checked:
				[x.setCheckState(0,Qt.Checked) for x in self.item_list]
			else:
				[x.setCheckState(0,Qt.Unchecked) for x in self.item_list]
		else:
			check_count = 0
			for x in self.item_list:
				if x.checkState(0) == Qt.Checked:
					check_count +=1
			if check_count ==5:
				self.qt5112.setCheckState(0,Qt.Checked)
			elif 0 < check_count < 5:
				self.qt5112.setCheckState(0,Qt.PartiallyChecked)
			else:
				self.qt5112.setCheckState(0,Qt.Unchecked)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Demo()
	demo.show()
	sys.exit(app.exec_())