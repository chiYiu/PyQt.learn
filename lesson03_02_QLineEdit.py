# -*- coding: utf-8 -*-
import sys
from PySide.QtGui import QApplication,QWidget,QLabel,QVBoxLayout,QLineEdit,QHBoxLayout

class Demo(QWidget):
    """docstring for Demo"""
    def __init__(self):
        super(Demo, self).__init__()
        self.user_label = QLabel("userrname:",self)
        self.user_line = QLineEdit(self)


        self.h_layout = QHBoxLayout()#实例化一个垂直布局管理器QVBoxLayout
        self.h_layout.addWidget(self.user_label)#调用addWidget()方法来将控件一个个添加到垂直布局中
        self.h_layout.addWidget(self.user_line)

        self.setLayout(self.h_layout)#将self.v_layout设为整个窗口的最终布局方式

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())