# -*- coding: utf-8 -*-
import sys
from PySide.QtGui import QApplication,QWidget,QLabel,QVBoxLayout

class Demo(QWidget):
    """docstring for Demo"""
    def __init__(self):
        super(Demo, self).__init__()
        self.user_label = QLabel("userrname:",self)
        self.pwd_label = QLabel("Password:",self)

        self.v_layout = QVBoxLayout()#实例化一个垂直布局管理器QVBoxLayout
        self.v_layout.addWidget(self.user_label)#调用addWidget()方法来将控件一个个添加到垂直布局中
        self.v_layout.addWidget(self.pwd_label)

        self.setLayout(self.v_layout)#将self.v_layout设为整个窗口的最终布局方式

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())