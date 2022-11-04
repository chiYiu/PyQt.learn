# -*- coding: utf-8 -*-


###停靠窗口QDockWidget###
#QDockWidget是要和QMainWindow一起搭配使用
#调用QDockWidget的setAllowedAreas()来可停靠的位置，可以传入的参数有：
#Qt.LeftDockWidgetArea			左边停靠区域
#Qt.RightDockWidgetArea         右边停靠区域
#Qt.TopDockWidgetArea 			顶部停靠区域
#Qt.BottomDockWidgetArea		底部停靠区域
#Qt.AllDockWidgetArea			全部停靠区域
#Qt.NoDockWidgetArea			不可停靠（将不显示Widget）
#除了设置停靠窗口的停靠位置，
#我们也还可以调用setFeatures()方法来设置停靠窗口的功能属性
#QDockWidget.DockWidgetClosable            可关闭停靠窗口
#QDockWidget.DockWidgetMovable	      	   停靠窗口可在停靠区域移动
#QDockWidget.DockWidgetFloattable		   停靠窗口可与主窗口分离 
#QDockWidget.DockWidgetVerticalTitleBar    停靠窗口中的左侧显示一个标签
#QDockWidget.AllDockWidgetFeatures         前三种全部功能，可关闭，可移动和可浮动
#QDockWidget.NoDockWidgetFeatures          停靠窗口无法关闭移动和浮动
import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication,QMainWindow,QDockWidget,QTextEdit

class Demo(QMainWindow):
	"""docstring for Demo"""
	def __init__(self):
		super(Demo, self).__init__()
		#实例化三个停靠窗口，在实例化的时候直接设置好窗口的标题
		self.dock1 = QDockWidget('Dock Window 1',self)
		self.dock2 = QDockWidget('Dock Window 2',self)
		self.dock3 = QDockWidget('Dock Window 3',self)
		#设置三个停靠窗口的可停靠区域
		self.dock1.setAllowedAreas(Qt.RightDockWidgetArea|Qt.LeftDockWidgetArea)
		self.dock2.setAllowedAreas(Qt.RightDockWidgetArea|Qt.TopDockWidgetArea)
		self.dock3.setAllowedAreas(Qt.NoDockWidgetArea)
		#设置三个停靠窗口的功能属性，因为我们在第二步中对dock3设置为不可停靠，
		#所在这步中就只用设置可关闭的功能属性就好了
		self.dock1.setFeatures(QDockWidget.DockWidgetMovable|QDockWidget.DockWidgetFloatable)
		self.dock2.setFeatures(QDockWidget.DockWidgetMovable|QDockWidget.DockWidgetClosable)
		self.dock3.setFeatures(QDockWidget.AllDockWidgetFeatures)
		#实例化三个文本编辑框QTextEdit，然后调用QDockWidget的setWidget()方法将文本编辑框放入停靠窗口中
		self.text1 = QTextEdit()
		self.text2 = QTextEdit()
		self.text3 = QTextEdit()

		self.dock1.setWidget(self.text1)
		self.dock2.setWidget(self.text2)
		self.dock3.setWidget(self.text3)

		#调用主窗口的addDockWidget()方法将停靠窗口加入到主窗口中，注意要规定停靠窗口刚开始的停靠区域
		self.addDockWidget(Qt.RightDockWidgetArea,self.dock1)
		self.addDockWidget(Qt.RightDockWidgetArea,self.dock2)
		self.addDockWidget(Qt.RightDockWidgetArea,self.dock3)

		#设置主窗口的中央控件
		self.center_text = QTextEdit()
		self.setCentralWidget(self.center_text)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Demo()
	demo.show()
	sys.exit(app.exec_())