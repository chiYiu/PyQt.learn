# -*- coding: utf-8 -*-
#窗口QSplitter、标签页窗口QTabWidget、堆叠窗口QStackedWidget、停靠窗口QDockWidget以及多文档界面QMidiArea
#这些类可以帮助我们加入更多的控件，更多的功能，而且不会让界面看起来混乱


###标签页窗口QTabWidget###
import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication,QWidget,QTabWidget,QLabel,QLineEdit,QDateEdit,\
						QComboBox,QTextEdit,QGridLayout,QIcon
		
class Demo(QTabWidget):
    #继承QSplitter
	def __init__(self):
		super(Demo, self).__init__()
		self.tab1 = QWidget()
		self.tab2 = QWidget()
		self.tab3 = QTextEdit()
		#实例化两个QWidget窗口和一个QTextEdit控件

		self.tab1_init()
		self.tab2_init()
		
		self.addTab(self.tab1,'Basic Info')
		self.addTab(self.tab2,'Contact Info')
		self.addTab(self.tab3,QIcon('images/info.ico'),'More Info')
		
		self.currentChanged.connect(self.print_index)

	def print_index(self):
		print(self.currentIndex())

	def tab1_init(self):
		name_label = QLabel('Name:',self.tab1)
		gender_label = QLabel('Gender:',self.tab1)
		bd_label = QLabel('Birth Date',self.tab1)

		name_line = QLineEdit(self.tab1)
		items = ['Please choose your gender','Female','Male']
		gender_combo = QComboBox(self.tab1)
		gender_combo.addItems(items)
		bd_dateedit = QDateEdit(self.tab1)

		g_layout = QGridLayout()
		g_layout.addWidget(name_label,0,0,1,1)
		g_layout.addWidget(name_line,0,1,1,1)
		g_layout.addWidget(gender_label,1,0,1,1)
		g_layout.addWidget(gender_combo,1,1,1,1)
		g_layout.addWidget(bd_label,2,0,1,1)
		g_layout.addWidget(bd_dateedit,2,1,1,1)
		self.tab1.setLayout(g_layout)


	def tab2_init(self):
		tel_label = QLabel('Tel:',self.tab2)
		mobile_label = QLabel('Mobile',self.tab2)
		add_label = QLabel('Address',self.tab2)

		tel_line = QLineEdit(self.tab2)
		mobile_line = QLineEdit(self.tab2)
		add_line = QLineEdit(self.tab2)

		g_layout = QGridLayout()
		g_layout.addWidget(tel_label,0,0,1,1)
		g_layout.addWidget(tel_line,0,1,1,1)
		g_layout.addWidget(mobile_label,1,0,1,1)
		g_layout.addWidget(mobile_line,1,1,1,1)
		g_layout.addWidget(add_label,2,0,1,1)
		g_layout.addWidget(add_line,2,1,1,1)
		
		self.tab2.setLayout(g_layout)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Demo()
	demo.show()
	sys.exit(app.exec_())