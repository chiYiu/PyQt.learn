# -*- coding: utf-8 -*-
import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication, QWidget, QDial,QLabel,QVBoxLayout,QHBoxLayout,QFont

#滑动条QSlider和表盘QDial
class Demo(QWidget):
    """docstring for Demo"""
    def __init__(self):
        super(Demo, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowTitle('QDial')

        self.dial = QDial(self)
        self.dial.setFixedSize(100,100)
        self.dial.setRange(0,100)
        self.dial.setNotchesVisible(True)
        self.dial.valueChanged.connect(self.on_change_func)

        self.label = QLabel('0',self)
        self.label.setFont(QFont('Arial Black',20))

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.dial)
        self.h_layout.addWidget(self.label)

        self.setLayout(self.h_layout)

    def on_change_func(self):
        self.label.setText(str(self.dial.value()))

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec_())