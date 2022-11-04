# -*- coding: utf-8 -*-
import sys
from PySide.QtGui import QApplication, QWidget, QSpinBox,QDoubleSpinBox,QHBoxLayout

##数字调节框
class Demo(QWidget):
    choice = 'a'
    choice_list = ['b','c','d','e']
    """docstring for Demo"""
    def __init__(self):
        super(Demo, self).__init__()
        self.spinbox = QSpinBox(self)
        self.spinbox.setRange(-99,990)
        self.spinbox.setSingleStep(1)
        self.spinbox.setValue(66)
        self.spinbox.valueChanged.connect(self.value_hange_func)

        self.doubule_spinbox = QDoubleSpinBox(self)
        self.doubule_spinbox.setRange(-99.99,99.99)
        self.doubule_spinbox.setSingleStep(0.01)
        self.doubule_spinbox.setValue(66.66)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.spinbox)
        self.h_layout.addWidget(self.doubule_spinbox)
        self.setLayout(self.h_layout)

    def value_hange_func(self):
        decimal_part = self.doubule_spinbox.value() - int(self.doubule_spinbox.value())

        self.doubule_spinbox.setValue(self.spinbox.value()+decimal_part)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec_())