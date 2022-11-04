# -*- coding: utf-8 -*-

###堆叠窗口QStackedWidget###

#QStackedWidget用法跟QTabWdidget用法思想相似，只是界面样式不同。
#我们经常将QStackedWidget和QListWidget或者QListView搭配使用
import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication,QWidget,QStackedWidget,QLabel,QLineEdit,QDateEdit,\
						QComboBox,QTextEdit,QListView,QListWidget,QGridLayout,QHBoxLayout
		
class Demo(QWidget):
    #继承QWidget
	def __init__(self):
		super(Demo, self).__init__()

		self.stack1 = QWidget()
		self.stack2 = QWidget()
		self.stack3 = QTextEdit()


		self.stack1_init()
		self.stack2_init()

		self.stacked_widget = QStackedWidget(self)
		##实例化一个QStackedWidget窗口
		self.stacked_widget.addWidget(self.stack1)
		self.stacked_widget.addWidget(self.stack2)
		self.stacked_widget.addWidget(self.stack3)
		self.stacked_widget.currentChanged.connect(lambda:self.print_index)
		#将我们已经在stack1_init()和stack2_init()函数中设置好的窗口以及QTextEdit控件添加进去，
		#并且进行信号和槽的连接，每当堆叠层发生变化时，打印相应的索引

		self.list_widget = QListWidget(self)
		self.list_widget.addItem('Basic Info')
		self.list_widget.addItem('Contact Info')
		self.list_widget.addItem('More Info')
		self.list_widget.clicked.connect(self.change_func)



		self.h_layout = QHBoxLayout()
		self.h_layout.addWidget(self.list_widget)
		self.h_layout.addWidget(self.stacked_widget)
		self.setLayout(self.h_layout)
		#将QStackedWidget和QListWidget放在该窗口中


	def print_index(self):
		print(self.stacked_widget.currentIndex())

	def stack1_init(self):
		name_label = QLabel('Name:',self.stack1)
		gender_label = QLabel('Gender:',self.stack1)
		bd_label = QLabel('Birth Date:',self.stack1)

		name_line = QLineEdit(self.stack1)
		items = ['Please choose your gender', 'Female', 'Male']
		gender_combo = QComboBox(self.stack1)
		gender_combo.addItems(items)
		bd_dateedit = QDateEdit(self.stack1)

		g_layout = QGridLayout()
		g_layout.addWidget(name_label,0,0,1,1)
		g_layout.addWidget(name_line,0,1,1,1)
		g_layout.addWidget(gender_label,1,0,1,1)
		g_layout.addWidget(gender_combo,1,1,1,1)
		g_layout.addWidget(bd_label,2,0,1,1)
		g_layout.addWidget(bd_dateedit,2,1,1,1)

		self.stack1.setLayout(g_layout)

	def stack2_init(self):
		tel_label = QLabel('Tel:',self.stack2)
		mobile_label = QLabel('Mobile:',self.stack2)
		add_label = QLabel('Address:',self.stack2)

		tel_line = QLineEdit(self.stack2)
		mobile_line = QLineEdit(self.stack2)
		add_line = QLineEdit(self.stack2)

		g_layout = QGridLayout()
		g_layout.addWidget(tel_label,0,0,1,1)
		g_layout.addWidget(tel_line,0,1,1,1)
		g_layout.addWidget(mobile_label,1,0,1,1)
		g_layout.addWidget(mobile_line,1,1,1,1)
		g_layout.addWidget(add_label,2,0,1,1)
		g_layout.addWidget(add_line,2,1,1,1)

		self.stack2.setLayout(g_layout)

	def change_func(self):
		self.stacked_widget.setCurrentIndex(self.list_widget.currentIndex().row())
		#每当用户点击列表控件中不同行时，QStackedWidget调用setCurrentIndex(int)方法传入索引将显示界面设为相应的堆叠层
		

if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Demo()
	demo.show()
	sys.exit(app.exec_())