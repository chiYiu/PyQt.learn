# -*- coding: utf-8 -*-
####事件处理####

###鼠标事件重写###鼠标移动、按下或者释放动作都会唤起相应的鼠标事件
import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication, QWidget, QLabel, QVBoxLayout

class Demo(QWidget):
    """docstring for Demo"""
    def __init__(self):
        super(Demo, self).__init__()
        self.button_label = QLabel('No Button Pressed', self)#button_label用来显示鼠标的点击和释放动作
        self.xy_label = QLabel('x:0,y:0',self)#xy_label用于记录鼠标相对于QWidget窗口的坐标；
        self.global_xy_label = QLabel('global x:0,global y:0',self)#global_xy_label用于记录鼠标相对于显示屏屏幕的坐标；

        self.button_label.setAlignment(Qt.AlignCenter)
        self.xy_label.setAlignment(Qt.AlignCenter)
        self.global_xy_label.setAlignment(Qt.AlignCenter)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.button_label)
        self.v_layout.addWidget(self.xy_label)
        self.v_layout.addWidget(self.global_xy_label)
        self.setLayout(self.v_layout)

        self.resize(300,300)
        self.setMouseTracking(True)
        #setMouseTracking(True)方法可以让窗口始终追踪鼠标，否则只能每次等鼠标被点击后，
        #窗口才会开始记录鼠标的动作变化；而鼠标释放后，窗口又会不进行记录了，这样比较麻烦。

    def mouseMoveEvent(self,QMouseEvent):
        x = QMouseEvent.x()
        y = QMouseEvent.y()
        global_x = QMouseEvent.globalX()
        global_y = QMouseEvent.globalY()

        self.xy_label.setText('x:{},y:{}'.format(x,y))
        self.global_xy_label.setText('global x:{},global y:{}'.format(global_x,global_y))
        #mouseMoveEvent()为鼠标移动时所触发的响应函数，在函数中，
        #我们通过x()和y()方法获取鼠标相对于QWidget窗口的坐标，用globalX()和globalY()方法获取鼠标相对于显示屏屏幕的坐标；

    def mousePressEvent(self,QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.button_label.setText('Left Button Pressed')
        elif QMouseEvent.button() == Qt.MidButton:
            self.button_label.setText('Middle Button Pressed')
        elif QMouseEvent.button() == Qt.RightButton:
            self.button_label.setText('Right Button Pressed')
        #mousePressEvent()为鼠标被按下时所触发的响应函数，在函数中，我们通过button()方法来确认被按下的键，
        #然后用button_label显示被按下的键
    def mouseReleaseEvent(self,QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.button_label.setText('Left Button Released')
        elif QMouseEvent.button() == Qt.MidButton:
            self.button_label.setText('Middle Button Released')
        elif QMouseEvent.button() == Qt.RightButton:
            self.button_label.setText('Right Button Released')
        #mouseReleaseEvent()为鼠标释放时所触发的响应函数，同理，在函数中，我们通过button()方法来确认被释放的键，
        #然后用button_label显示被释放的键；
    def mouseDoubleClickEvent(self,QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.button_label.setText('Left Button Double Clicked')
        elif QMouseEvent.button() == Qt.MidButton:
            self.button_label.setText('Middle Button Double Clicked')
        elif QMouseEvent.button() == Qt.RightButton:
            self.button_label.setText('Right Button Double Clicked')
        #mouseDoubleClickEvent()为鼠标被双击时所触发的响应函数，同理，在函数中，
        #我们通过button()方法来确认被双击的键，然后用button_label显示被双击的键；

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())