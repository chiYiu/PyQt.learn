# -*- coding: utf-8 -*-
####事件处理####

###鼠标事件重写###鼠标移动、按下或者释放动作都会唤起相应的鼠标事件
#### 剪贴板
import sys ##引用sys模块进来，并不是进行sys的第一次加载 
reload(sys) #重新加载sys
sys.setdefaultencoding('utf-8') ###调用setdefaultencoding函数

from PySide.QtCore import Qt
from PySide.QtGui import QApplication, QWidget,QTextEdit,QTextBrowser,QPushButton,QGridLayout

class Demo(QWidget):
    """docstring for Demo"""
    def __init__(self):
        super(Demo, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowTitle(u"剪贴板")

        self.text_edit = QTextEdit(self)
        #实例化文本编辑text_edit控件
        self.text_browser = QTextBrowser(self)
        #实例化文本显示text_browser控件

        self.clipboard = QApplication.clipboard()
        #实例化一个剪贴板
        self.clipboard.dataChanged.connect(self.printf)
        #将剪贴板的dataChanged信号和打印函数连接起来，每当剪贴板内容发生变化的时候，
        #都会触发dataChanged信号，也就是说一旦变化就打印出Data Changed
        self.copy_btn = QPushButton('Copy',self)
        #实例化按钮copy_btn
        self.copy_btn.clicked.connect(self.copy_func)
        #连接按钮copy_btn的clicked信号与copy_func

        self.paste_btn = QPushButton('Paste',self)
        #实例化按钮copy_btn
        self.paste_btn.clicked.connect(self.paste_func)
        #连接按钮paste_btn的clicked信号与paste_func


        self.g_layout = QGridLayout()
        #实例化网格布局
        self.g_layout.addWidget(self.text_edit,0,0,1,1)
        self.g_layout.addWidget(self.text_browser,0,1,1,1)
        self.g_layout.addWidget(self.copy_btn,1,0,1,1)
        self.g_layout.addWidget(self.paste_btn,1,1,1,1)
        #设置网格布局位置
        self.setLayout(self.g_layout)
        #设置最终布局

    def printf(self):
        print('Data Changed')

    def copy_func(self):
        self.clipboard.setText(self.text_edit.toPlainText())

    #将text_edit中的文本获取过来并通过setText()方法将其设置为剪贴板的文本
    #需要解码
    #############
    def paste_func(self):
        mime = self.clipboard.mimeData()
        if mime.hasText():
            self.text_browser.setText(u'%s' %mime.text().encode('utf-8'))
    #我们将text_browser的文本设为剪贴板的文本

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())