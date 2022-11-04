# -*- coding: utf-8 -*-
#数据库#
#数据库连接和关闭
#在用到数据库的程序中，我们通常把数据库连接操作放在程序应用开始时(因为数据库无法连接的话，程序的功能就会收到影响了，所以要先确保数据库连接成功)。
#首先来看一下连接SQLite数据库：

import sys
from PySide.QtSql import QSqlDatabase
from PySide.QtGui import QApplication,QWidget,QMessageBox

class Demo(QWidget):
	def __init__(self):
		super(Demo,self).__init__()
		self.db = None
		self.db_connect()

	def db_connect(self):
		self.db = QSqlDatabase.addDatabase('QSQLITE')
		#QSqlDatabase类的addDatabase()方法来创建一个数据库连接SQLite数据库
		self.db.setDatabaseName('./test.db')
		#调用setDatabaseName()设置要使用的数据库名称，只需要写入一个路径
		if not self.db.open():
			QMessageBox.critical(self,'Database connection',self.db.lastError().text())
			#调用open()方法打开数据库，若打开成功则返回True，失败则返回False。
			#在这里我们用消息框来提示用户数据库打开失败，lastErrot().text()方法可以获取数据库打开失败的原因

	def closeEvent(self,QcloseEvent):
		self.db.close()
		#在窗口关闭事件中通过self.db.close()方法来关闭数据库

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())