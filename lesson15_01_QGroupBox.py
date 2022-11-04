# -*- coding: utf-8 -*-
import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication, QWidget, QGroupBox,QRadioButton,QLabel,\
                        QVBoxLayout,QHBoxLayout,QPixmap

#组合框QGroupBox和工具箱QToolBox

class Demo(QWidget):
    """docstring for Demo"""
    def __init__(self):
        super(Demo, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowTitle('QGroupBox')

        self.groupbox_1 = QGroupBox('On and Off',self)
        self.groupbox_2 = QGroupBox('Change Color',self)
        #实例化两个QGroupBox组合框，第一个用来放置On和Off单选按钮，第二个用来放置各种颜色按钮

        self.red = QRadioButton('Red',self)
        self.blue = QRadioButton('Blue',self)
        self.green = QRadioButton('Green',self)
        self.yellow = QRadioButton('Yellow',self)
        self.color_list = [self.red,self.blue,self.green,self.yellow]
        #实例化各个颜色按钮，并将它们放在一个列表中，方便之后使用列表推导式来简化代码

        self.on = QRadioButton('On',self)
        self.off = QRadioButton('Off',self)
        #实例化On和Off单选按钮

        self.pic_label = QLabel(self)
        #实例化一个QLabel控件，用于显示图片

        self.h1_layout = QHBoxLayout()
        self.h2_layout = QHBoxLayout()
        self.h3_layout = QHBoxLayout()
        self.all_layout = QVBoxLayout()

        self.layout_init()
        self.radiobutton_init()
        self.label_init()

    def layout_init(self):
        self.h1_layout.addWidget(self.on)
        self.h1_layout.addWidget(self.off)
        self.groupbox_1.setLayout(self.h1_layout)

        self.h2_layout.addWidget(self.red)
        self.h2_layout.addWidget(self.blue)
        self.h2_layout.addWidget(self.green)
        self.h2_layout.addWidget(self.yellow)
        self.groupbox_2.setLayout(self.h2_layout)

        self.h3_layout.addWidget(self.groupbox_1)
        self.h3_layout.addWidget(self.groupbox_2)

        self.all_layout.addWidget(self.pic_label)
        self.all_layout.addLayout(self.h3_layout)


        self.setLayout(self.all_layout)

    def radiobutton_init(self):
        self.yellow.setChecked(True)
        for btn in self.color_list:
            btn.clicked.connect(self.change_color_func)

        self.off.setChecked(True)
        self.off.toggled.connect(self.on_and_off_func)
        #在radiobutton_init()函数中，我们先将yellow单选按钮设置为已点击状态，
        #然后用各个颜色按钮的clicked信号与自定义的槽函数change_color_func()连接起来

    def label_init(self):
        self.pic_label.setPixmap(QPixmap('images/off.png'))
        self.pic_label.setAlignment(Qt.AlignCenter)
        #将刚开始显示的QLabel图片设置为Off.png，然后让其居中显示
        
    def change_color_func(self):
        if self.on.isChecked():
            path = 'images/{}.png'.format([btn.text() for btn in self.color_list if btn.isChecked()][0])
            self.pic_label.setPixmap(QPixmap(path))

    def on_and_off_func(self):
        if self.on.isChecked():
            path =  path = 'images/{}.png'.format([btn.text() for btn in self.color_list if btn.isChecked()][0])
            self.pic_label.setPixmap(QPixmap(path))
        else:
            self.pic_label.setPixmap(QPixmap('images/off.png'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())