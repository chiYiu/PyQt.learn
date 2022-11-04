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