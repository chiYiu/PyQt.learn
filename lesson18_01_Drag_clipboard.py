# -*- coding: utf-8 -*-
####事件处理####

###鼠标事件重写###鼠标移动、按下或者释放动作都会唤起相应的鼠标事件
import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication, QTextBrowser,QTextEdit

#DragEnterEvent: 所拖动目标进入接收该事件的窗口或控件时触发；
#DragMoveEvent: 所拖动目标进入窗口或控件后，继续被拖动时触发；
#DragLeaveEvent: 所拖动目标离开窗口或控件时触发；
#DropEvent: 所拖动目标被放下时触发。
class Demo(QTextBrowser):
    #继承QTextBrowser，也就是说下面来实现该控件的拖放事件响应函数
    """docstring for Demo"""
    def __init__(self):
        super(Demo, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowTitle(u"拖放与剪贴板")
        self.setAcceptDrops(True)
        #setAcceptDrops(True)方法可以让该控件接收放下(Drop)事件；

    def dragEnterEvent(self,QDragEnterEvent):
        if QDragEnterEvent.mimeData().hasText():
            print('Drag Enter')
            QDragEnterEvent.acceptProposedAction()
        else:
            QDragEnterEvent.ignore()
    #当拖动目标进入QTextBrowser的那一刹那，触发dragEnterEvent事件，在该响应函数中，
    #我们先判断所拖动目标的MIME类型是否为text/plain，
    #若是的话则调用acceptProposedAction()方法来表明可以在QTextBrowser上进行拖放动作
    def dragMoveEvent(self,QDragMoveEvent):
        if QDragMoveEvent.mimeData().hasText():
            QDragMoveEvent.accept()
            print('Drag Move')
        else:
            QDragMoveEvent.ignore()
    #当目标进入窗体后，如果不放下而是继续移动的话，则会触发dragMoveEvent事件     
    def dragLeaveEvent(self,QDragLeaveEvent):
        print('Drag Leave')
     # 将进入控件后的目标再次拖动到控件之外时，就会触发dragLeaveEvent()事件
    def dropEvent(self, QDropEvent):
        if QDropEvent.mimeData().hasText():
            print('Drag Drop')
            txt_path = QDropEvent.mimeData().text().replace('file:///', '')
            with open(txt_path, 'r') as f:
                self.setText(f.read())
    #将目标在QTextBrowser中放下后，我们先通过QDropEvent.mimeData().text()方法获取到该文件的URI路径，
    #replace()方法将其中的file:///替换为/，这样得到的值才是我们想要的本地文件路径。
    #最后打开my.txt文件进行读取，并用setText()方法将QTextBrowser的文本设为该my.txt的内容
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

    ###应该是权限不足，在maya里面调试可以运行