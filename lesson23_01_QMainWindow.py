# -*- coding: utf-8 -*-
#主窗口QMainWindow##

import sys
from PySide.QtCore import Qt,QMimeData
from PySide.QtGui import QApplication,QMainWindow,QTextEdit,QAction,QFileDialog,\
						QMessageBox,QFontDialog,QColorDialog,QIcon
##python 2.6需要加下面这几行
#######################
import sys ##引用sys模块进来，并不是进行sys的第一次加载 
reload(sys) #重新加载sys
sys.setdefaultencoding('utf-8') ###调用setdefaultencoding函数
#########################

class Demo(QMainWindow):
	is_saved = True
	is_saved_first = True
	path = ''
	#设置变量，判断文本是否保存，是否第一次保存以及用于文件路径保存
	def __init__(self):
		super(Demo, self).__init__()
		self.file_menu = self.menuBar().addMenu('File')
		self.edit_menu = self.menuBar().addMenu('Edit')
		self.help_menu = self.menuBar().addMenu('Help')

		self.file_toobar = self.addToolBar('File')
		self.edit_toobar = self.addToolBar('Edit')

		self.status_bar = self.statusBar()
		#添加实例化菜单栏、工具栏和状态栏

		self.new_action = QAction('New',self)
		self.open_action = QAction('Open',self)
		self.save_action = QAction('Save',self)
		self.save_as_action = QAction('Save As',self)
		self.close_action = QAction('Close',self)
		self.cut_action = QAction('Cut',self)
		self.copy_action = QAction('Copy',self)
		self.paste_action = QAction('Paste',self)
		self.font_action = QAction('Font',self)
		self.color_action = QAction('Color',self)
		self.about_action = QAction('QT',self)
		#实例化11个动作

		self.text_edit = QTextEdit(self)
		#实例化一个QTextEdit控件

		self.mime_data = QMimeData()
		##实例化QMimeData类
		self.clipboard = QApplication.clipboard()
		#创建一个剪辑板

		self.setCentralWidget(self.text_edit)
		#调用QMainWindow的setCentralWidget()方法设置主窗口的中央控件
		self.resize(450,600)

		#在代码量比较多的情况下，将各个对象分开来设置会让代码更加清晰，
		#如果都同时挤在__init__()中的话会显得非常混乱，也不方便日后维护
		self.menu_init()
		self.toolbar_init()
		self.status_bar_init()
		self.action_init()
		self.text_edit_init()

	def menu_init(self):
		self.file_menu.addAction(self.new_action)
		self.file_menu.addAction(self.open_action)
		self.file_menu.addAction(self.save_action)
		self.file_menu.addAction(self.save_as_action)
		self.file_menu.addSeparator()
		self.file_menu.addAction(self.close_action)

		self.edit_menu.addAction(self.cut_action)
		self.edit_menu.addAction(self.copy_action)
		self.edit_menu.addAction(self.paste_action)
		self.edit_menu.addSeparator()
		self.edit_menu.addAction(self.font_action)
		self.edit_menu.addAction(self.color_action)

		self.help_menu.addAction(self.about_action)
	#调用addAction()方法就可以将动作添加进去。addSeparator()方法顾名思义就是加一个分割条

	def toolbar_init(self):
		self.file_toobar.addAction(self.new_action)
		self.file_toobar.addAction(self.open_action)
		self.file_toobar.addAction(self.save_action)
		self.file_toobar.addAction(self.save_as_action)
		self.file_toobar.addAction(self.close_action)
		self.edit_toobar.addAction(self.cut_action)
		self.edit_toobar.addAction(self.copy_action)
		self.edit_toobar.addAction(self.paste_action)
		self.edit_toobar.addAction(self.font_action)
		self.edit_toobar.addAction(self.color_action)

	def status_bar_init(self):
		self.status_bar.showMessage('Ready to compose')
	#状态栏设置调用showMessage()方法

	def action_init(self):
		self.new_action.setIcon(QIcon('images/textImage/new.ico'))
		#通过setIcon()方法传入QIcon参数来设置动作的图标
		self.new_action.setShortcut('Ctrl+N')
		#setShortCut()方法就是用来设置快捷键的,将快捷键设置为Ctrl+N
		self.new_action.setToolTip('Create a new file')
		#setToolTip()方法可以用来设置小气泡提示，当鼠标停留在该动作上时，就会显示相应的提示
		self.new_action.setStatusTip('Create a new file')
		#setStatusTip()就是设置状态栏信息，当鼠标停留在该动作上时，状态栏会显示相应的信息
		self.new_action.triggered.connect(self.new_func)
		#将new_action的triggered信号与自定义的槽函数连接起来

		self.open_action.setIcon(QIcon('images/textImage/open.ico'))
		self.open_action.setShortcut('Ctrl+O')
		self.open_action.setToolTip('Open a exiting file')
		self.open_action.setStatusTip('Open a exiting file')
		self.open_action.triggered.connect(self.open_file_func)

		self.save_action.setIcon(QIcon('images/textImage/save.ico'))
		self.save_action.setShortcut('Ctrl+S')
		self.save_action.setToolTip('Save the file')
		self.save_action.setStatusTip('Save the file')
		self.save_action.triggered.connect(lambda:self.save_func(self.text_edit.toHtml()))

		self.save_as_action.setIcon(QIcon('images/textImage/save_as.ico'))
		self.save_as_action.setShortcut('Ctrl+A')
		self.save_as_action.setToolTip('Save the file to a specified location')
		self.save_as_action.setStatusTip('Save the file to a specified location')
		self.save_as_action.triggered.connect(lambda:self.save_as_func(self.text_edit.toHtml()))

		self.close_action.setIcon(QIcon('images/textImage/close.ico'))
		self.close_action.setShortcut('Ctrl+E')
		self.close_action.setToolTip('Close the window')
		self.close_action.setStatusTip('Close the window')
		self.close_action.triggered.connect(self.close_func)

		self.cut_action.setIcon(QIcon('images/textImage/cut.ico'))
		self.cut_action.setShortcut('Ctrl+X')
		self.cut_action.setToolTip('Cut the text to clipboard')
		self.cut_action.setStatusTip('Cut the text to clipboard')
		self.cut_action.triggered.connect(self.cut_func)

		self.copy_action.setIcon(QIcon('images/textImage/copy.ico'))
		self.copy_action.setShortcut('Ctrl+C')
		self.copy_action.setToolTip('Copy the text')
		self.copy_action.setStatusTip('Save the file')
		self.copy_action.triggered.connect(self.copy_func)

		self.paste_action.setIcon(QIcon('images/textImage/paste.ico'))
		self.paste_action.setShortcut('Ctrl+V')
		self.paste_action.setToolTip('Paste the text')
		self.paste_action.setStatusTip('Paste the text')
		self.paste_action.triggered.connect(self.paste_func)

		self.font_action.setIcon(QIcon('images/textImage/font.ico'))
		self.font_action.setShortcut('Ctrl+T')
		self.font_action.setToolTip('Change the font')
		self.font_action.setStatusTip('Change the font')
		self.font_action.triggered.connect(self.font_func)

		self.color_action.setIcon(QIcon('images/textImage/color.ico'))
		self.color_action.setShortcut('Ctrl+R')
		self.color_action.setToolTip('Change the color')
		self.color_action.setStatusTip('Change the color')
		self.color_action.triggered.connect(self.color_func)

		self.about_action.setIcon(QIcon('images/textImage/about.ico'))
		self.about_action.setShortcut('Ctrl+Q')
		self.about_action.setToolTip('What is Qt?')
		self.about_action.setStatusTip('What is Qt?')
		self.about_action.triggered.connect(self.about_func)

	def text_edit_init(self):
		self.text_edit.textChanged.connect(self.text_changed_func)

	def new_func(self):
		if not self.is_saved and self.text_edit.toPlainText():
			#新建前我们要判断当前文本是否有保存，如果没有的话，那就出现弹框询问是否要保存
			choice = QMessageBox.question(self,'','Do you want to save the text?',
										QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
			if choice == QMessageBox.Yes:
				self.save_func(self.text_edit.toHtml())
				self.text_edit.clear()
				self.is_saved_first = True
			elif choice == QMessageBox.No:
				self.text_edit.clear()
			#按Yes的话就调用save_func()函数进行保存(save_func()等函数
			#若按No不进行保存的话，就直接清空。若按下Cancel取消的话，则不进行任何动作
			else:
				pass
		else:
			self.text_edit.clear()
			self.is_saved = False
			self.is_saved_first = True
		#如果已经保存了，那么就直接清空文本编辑框，并设置相应变量就行了


	def open_file_func(self):
		if not self.is_saved:
			choice = QMessageBox.question(self,'','Do you want to save the text?',
										QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
			if choice == QMessageBox.Yes:
				self.save_func(self.text_edit.toHtml())
				file,_=QFileDialog.getOpenFileName(self,'Open File','./','file (*.html *.txt *.log)')
				if file:
					with open(file,'r') as f:
						self.text_edit.clear()
						self.text_edit.setText(u'%s' %f.read())
						self.is_saved = True
			elif choice == QMessageBox.No:
				file, _ = QFileDialog.getOpenFileName(self, 'Open File', './', 'Files (*.html *.txt *.log)')
				if file:
					with open(file, 'r') as f:
						self.text_edit.clear()
						self.text_edit.setText(u'%s' %f.read())
						self.is_saved = True
			else:
				pass
		else:
			file, _ = QFileDialog.getOpenFileName(self, 'Open File', './', 'Files (*.html *.txt *.log)')
			if file:
				with open(file, 'r') as f:
					self.text_edit.clear()
					self.text_edit.setText(u'%s' %f.read())
					self.is_saved = True




	def save_func(self,text):
		if self.is_saved_first:
			self.save_as_func(text)
		else:
			with open(self.path,'w') as f:
				f.write(u'%s' %text)
			self.is_saved = True

	def save_as_func(self,text):
		self.path,_ = QFileDialog.getSaveFileName(self,'Save File','./','file (*.html *.txt *.log)')
		print(self.path)
		print(_)
		if self.path:
			with open(self.path,'w') as f:
				f.write(u'%s' %text)
			self.is_saved = True
			self.is_saved_first = False

	def close_func(self):
		if not self.is_saved:
			choice = QMessageBox.question(self,'Save File','Do you want to save the text?',
										QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
			if choice == QMessageBox.Yes:
				self.save_func(self.text_edit.toHtml())
				self.close()
			elif choice == QMessageBox.No:
				self.close()
			else:
				pass
	def closeEvent(self,QCloseEvent):
		if not self.is_saved:
			choice = QMessageBox.question(self,'Save File','Do you want to save the text?',
										QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
			if choice == QMessageBox.Yes:
				self.save_func(self.text_edit.toHtml())
				QCloseEvent.accept()
			elif choice == QMessageBox.No:
				QCloseEvent.accept()
			else:
				QCloseEvent.ignore()



	def cut_func(self):
		self.mime_data.setHtml(self.text_edit.textCursor().selection().toHtml())
		self.clipboard.setMimeData(self.mime_data)
		self.text_edit.textCursor().removeSelectedText()

	def copy_func(self):
		self.mime_data.setHtml(self.text_edit.textCursor().selection().toHtml())
		self.clipboard.setMimeData(self.mime_data)

	def paste_func(self):
		self.text_edit.insertHtml(self.clipboard.mimeData().html())

	def font_func(self):
		font,ok = QFontDialog.getFont()
		if ok:
			self.text_edit.setFont(font)

	def color_func(self):
		color = QColorDialog.getColor()
		if color.isValid():
			self.text_edit.setTextColor(color)
	def about_func(self):
		QMessageBox.aboutQt(self,'About Qt')

	def text_changed_func(self):
		if self.text_edit.toPlainText():
			self.is_saved = False

		else:
			self.is_saved = True
		
		
		

if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Demo()
	demo.show()
	sys.exit(app.exec_())