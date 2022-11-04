# -*- coding: utf-8 -*-
import sys
from PySide.QtCore import Qt,QTimer
from PySide.QtGui import QApplication, QWidget, QLabel, QPushButton,QVBoxLayout

#定时器QTimer和进度条QProgressBar
class Demo(QWidget):
    """docstring for Demo"""
    def __init__(self):
        super(Demo, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowTitle('QTimer')

        self.label = QLabel('0',self)
        self.label.setAlignment(Qt.AlignCenter)

        self.step = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_func)

        self.ss_button = QPushButton('Start',self)
        self.ss_button.clicked.connect(self.start_stop_func)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.ss_button)

        self.setLayout(self.v_layout)

    def start_stop_func(self):
        if not self.timer.isActive():
            self.ss_button.setText('Stop')
            self.timer.start(100)
        else:
            self.ss_button.setText('Start')
            self.timer.stop()

    def update_func(self):
        self.step +=1
        self.label.setText(str(self.step))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())