# -*- coding: utf-8 -*-
#子控件
#我们知道QComboBox由一个矩形框和一个下拉按钮组成，而这个下拉按钮就是QComboBox的子控件了，
#PySide允许我们使用QSS对其进行样式化

import sys
from PySide.QtGui import QApplication,QComboBox

class Demo(QComboBox):
	def __init__(self):
		super(Demo,self).__init__()
		my_list = ['A','B','C','D']
		self.addItems(my_list)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Demo()
	qss = 'QComboBox::drop-down {image: url(images/drop-down.png)}'
	#通过在控件名后面加两个英文状态下的冒号::然后再写要获取的子控件drop-down就可以了
	#这里我们把QComboBox的子控件的图片换成了我们自已定义的(注意将drop-down.png图片文件放到项目目录中)
	demo.setStyleSheet(qss)
	demo.show()
	sys.exit(app.exec_())