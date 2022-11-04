# -*- coding: utf-8 -*-

#颜色对话框和字体对话框

import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication,QWidget,QTextEdit,QColorDialog,QPushButton,\
						QHBoxLayout,QVBoxLayout,QFontDialog

class Demo(QWidget):
	"""docstring for Demo"""
	def __init__(self):
		super(Demo, self).__init__()
		self.text_edit = QTextEdit(self)
		#QTextEdit控件用于显示文本颜色和字体变化

		self.color_btn = QPushButton('Color',self)
		self.font_btn = QPushButton('Font',self)
		self.color_btn.clicked.connect(lambda: self.open_dialog_func(self.color_btn))
		self.font_btn.clicked.connect(lambda: self.open_dialog_func(self.font_btn))

		self.h_layout = QHBoxLayout()
		self.h_layout.addWidget(self.color_btn)
		self.h_layout.addWidget(self.font_btn)

		self.v_layout = QVBoxLayout()
		self.v_layout.addWidget(self.text_edit)
		self.v_layout.addLayout(self.h_layout)
		self.setLayout(self.v_layout)

	def open_dialog_func(self,btn):
		if btn == self.color_btn:
			color = QColorDialog.getColor()
			#如果是color_btn被按下的话，则调用QColorDialog的getColor()方法显示颜色对话框
			#当选择一种颜色后其十六进制的值会保存在color变量中
			#但如果点击对话框中的取消(Cancel)按钮的话，则color为无效值。
			if color.isValid():
				self.text_edit.setTextColor(color)
			#通过isValid()方法判断color是否有效，
			#若有效的话则通过setTextColor()方法设置QTextEdit的文本颜色
		else:
			font,ok = QFontDialog.getFont()
			if ok:
				self.text_edit.setFont(font)

			#如果是font_btn被按下的话，则调用QFontDialog的getFont()方法显示字体对话框，该方法返回两个值，分别为QFont和bool值

		

if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Demo()
	demo.show()
	sys.exit(app.exec_())