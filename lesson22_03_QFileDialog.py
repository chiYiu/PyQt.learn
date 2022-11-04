# -*- coding: utf-8 -*-
#文件对话框
import sys ##引用sys模块进来，并不是进行sys的第一次加载 
reload(sys) #重新加载sys
sys.setdefaultencoding('utf-8') ###调用setdefaultencoding函数


import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication,QWidget,QTextEdit,QPushButton,QMessageBox,\
						QHBoxLayout,QVBoxLayout,QFileDialog

class Demo(QWidget):
	"""docstring for Demo"""
	def __init__(self):
		super(Demo, self).__init__()

		self.is_saved = True
		self.is_saved_first = True
		# is_saved_first变量用于判断是否是第一次进行保存，如果是的话则会打开文件对话框让用户选择路径，
		#填好文件名然后保存(即另存为)。如果不是第一次保存就说明之前保存过，那用户再点击保存按钮时程序就直接将文本保存在第一次保存时的路径
		self.path=''
		#path变量用于保存路径

		self.textedit = QTextEdit(self)
		self.textedit.textChanged.connect(self.on_textChanged_func)

		self.button = QPushButton('Save',self)
		self.button.clicked.connect(self.on_clicked_func)
		self.button_2 = QPushButton('Open',self)
		self.button_2.clicked.connect(self.open_file_func)

		self.h_layout =QHBoxLayout()
		self.h_layout.addWidget(self.button)
		self.h_layout.addWidget(self.button_2)
		self.v_layout = QVBoxLayout()
		self.v_layout.addWidget(self.textedit)
		self.v_layout.addLayout(self.h_layout)
		self.setLayout(self.v_layout)

	def on_textChanged_func(self):
		if self.textedit.toPlainText():
			self.is_saved = False
		else:
			self.is_saved = True

	def on_clicked_func(self):
		if self.is_saved_first:
			self.save_as_func(self.textedit.toPlainText())
		else:
			self.save_func(self.textedit.toPlainText())
	#在on_clicked_func()槽函数中，我们首先判断是不是第一次保存，是的话调用save_as_func()函数进行另存为操作
	def save_func(self,text):
		with open(self.path,'w') as f:
			f.write(u'%s' %text.encode('utf-8'))
		self.is_saved = True

	def save_as_func(self,text):
		self.path,_ = QFileDialog.getSaveFileName(self,'Save File','./','Files(*.txt &.log)')
		#调用QFileDialog的getSaveFileName(parent, str, strt, str)方法，第一个参数为指定父类，
		#第二个为文件对话框的标题，第三个为对话框打开时显示的路径，
		#最后一个为文件扩展名过滤器——对话框只会显示该过滤器所提供的扩展名
		#_指向被忽略的值
		if self.path:
			with open(self.path,'w') as f:
				f.write(u'%s' %text.encode('utf-8'))
			self.is_saved = True
			self.is_saved_first = False
		#当用户在对话框中选择好要保存的路径和文件名后，对话框返回绝对路径(我们保存在path中)和扩展过滤器，
		#这里我们用不到后者，所以直接就保存在_中。有了绝对路径后我们就可以使用with open()方法保存文本内容了
		#如果不是第一次保存的话，那说明path已经保存了第一次保存时的路径了，那我们就直接使用with open()方法进行保存就行了
	def open_file_func(self):
		file,_ = QFileDialog.getOpenFileName(self,'Save File','./','Files(*.txt &.log)')
		#调用QFileDialog的getOpenFileName(parent, str, str, str)方法，用法跟getSaveFileName()类似
		#

		print file
		if file:
			with open(file,'r') as f:
				self.textedit.clear()
				self.textedit.setText(f.read())
				self.is_saved = True
		#当用户选择了要开打的文件后，file值保存绝对路径，
		#我们用with open()方法打开读取，并将textedit的文本设为该文件内容。请小伙伴们思考下为什么这里要将is_save设为True
	def closeEvent(self,QCloseEvent):
		if not self.is_saved:
			choice = QMessageBox.question(self,'','Do you want to save the text?',
											QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
			if choice == QMessageBox.Yes:
				self.on_clicked_func()
				QCloseEvent.accept()
			elif choice == QMessageBox.No:
				QCloseEvent.accept()
			else:
				QCloseEvent.ignore()
	#在关闭窗口时，若用户点击Yes，则保存逻辑跟on_clicked_func()槽函数一样，
	#所以直接调用该槽函数就可以了(不过还是有点区别，因为此时is_saved和is_saved_first变量没必要修改了)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Demo()
	demo.show()
	sys.exit(app.exec_())