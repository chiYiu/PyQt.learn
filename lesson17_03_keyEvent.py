# -*- coding: utf-8 -*-
####事件处理####

###鼠标事件重写###鼠标移动、按下或者释放动作都会唤起相应的鼠标事件
import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication, QWidget, QLabel, QVBoxLayout, QPixmap

class Demo(QWidget):
    """docstring for Demo"""
    def __init__(self):
        super(Demo, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowTitle(u"鼠标事件")
        self.resize(250,100)

        self.pic_label = QLabel(self)
        self.pic_label.setPixmap(QPixmap('images/keyboard.png'))
        self.pic_label.setAlignment(Qt.AlignCenter)

        self.key_label = QLabel(u'空键盘',self)
        self.key_label.setAlignment(Qt.AlignCenter)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.pic_label)
        self.v_layout.addWidget(self.key_label)
        self.setLayout(self.v_layout)

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Up:
            self.pic_label.setPixmap(QPixmap('images/up.png'))
            self.key_label.setText(u'按下↑键')
        elif QKeyEvent.key() == Qt.Key_Down:
            self.pic_label.setPixmap(QPixmap('images/down.png'))
            self.key_label.setText(u'按下↓键')
        elif QKeyEvent.key() == Qt.Key_Left:
            self.pic_label.setPixmap(QPixmap('images/left.png'))
            self.key_label.setText(u'按下←键')
        elif QKeyEvent.key() == Qt.Key_Right:
            self.pic_label.setPixmap(QPixmap('images/right.png'))
            self.key_label.setText(u'按下→键')

    def keyReleaseEvent(self,QKeyEvent):
        self.pic_label.setPixmap(QPixmap('images/keyboard.png'))
        self.key_label.setText(u'释放键盘')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())