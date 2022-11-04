# -*- coding: utf-8 -*-
import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication, QWidget, QSlider,QLabel,QVBoxLayout,QHBoxLayout,QFont

#滑动条QSlider和表盘QDial
class Demo(QWidget):
    """docstring for Demo"""
    def __init__(self):
        super(Demo, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.slider_1 = QSlider(Qt.Horizontal,self)
        self.slider_1.setRange(0,100)
        self.slider_1.valueChanged.connect(lambda:self.on_change_func(self.slider_1))

        self.slider_2 = QSlider(Qt.Vertical,self)
        self.slider_2.setMinimum(0)
        self.slider_2.setMaximum(100)
        self.slider_2.valueChanged.connect(lambda:self.on_change_func(self.slider_2))

        self.label = QLabel('0',self)
        self.label.setFont(QFont('Arial Black',20))

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.h_layout.addWidget(self.slider_2)
        self.h_layout.addStretch(1)
        self.h_layout.addWidget(self.label)
        self.h_layout.addStretch(1)

        self.v_layout.addWidget(self.slider_1)
        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)

    def on_change_func(self,slider):
        if slider ==self.slider_1:
            self.slider_2.setValue(self.slider_1.value())
            self.label.setText(str(self.slider_1.value()))
        else:
            self.slider_1.setValue(self.slider_2.value())
            self.label.setText(str(self.slider_2.value()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec_())