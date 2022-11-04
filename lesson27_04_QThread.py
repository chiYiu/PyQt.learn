# -*- coding: utf-8 -*-
#要实现多线程，我们要先继承QThread类并重新实现其中的run()函数，
#也就是说把耗时的操作放入run()函数中。
#比如我们把上面例子的计数操作放在run()函数中

#点击按钮1，循环打印1，2，3。此时再次点击按钮1，
#在控制台会开启一个新的循环，我们期望在点击之后开始循环，在循环没有结束之前，
#此线程不允许使用。有两种解决办法：线程锁和信号
import sys
import time
import urllib2#python2
from PySide.QtCore import Qt,QThread,Signal,QMutex
from PySide.QtGui import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QHBoxLayout
class PreventFastClickThreadMutex(QThread):  # 线程1
    qmut = QMutex()  # 创建线程锁
    def __init__(self):
        super(PreventFastClickThreadMutex,self).__init__()


    def run(self):
        self.qmut.lock()  # 加锁
        values = [1, 2, 3, 4, 5]
        for i in values:
            print(i)
            time.sleep(0.5)  # 休眠
        self.qmut.unlock()  # 解锁


class PreventFastClickThreadSignal(QThread):  # 线程2
    _signal = Signal()

    def __init__(self):
        super(PreventFastClickThreadSignal,self).__init__()

    def run(self):
        values = ["a", "b", "c", "d", "e"]
        for i in values:
            print(i)
            time.sleep(0.5)
        self._signal.emit()


class MyWin(QWidget):
    def __init__(self):
        super(MyWin,self).__init__()
        # 按钮初始化
        self.btn_1 = QPushButton(u'按钮1', self)
        self.btn_1.setCheckable(True)
        self.btn_1.move(120, 80)
        self.btn_1.clicked.connect(self.click_1)  # 绑定槽函数

        self.btn_2 = QPushButton(u'按钮2', self)
        self.btn_2.setCheckable(True)
        self.btn_2.move(120, 120)
        self.btn_2.clicked.connect(self.click_2)  # 绑定槽函数

    def click_1(self):
        self.thread_1 = PreventFastClickThreadMutex()  # 创建线程
        self.thread_1.start()  # 开始线程

    def click_2(self):
        self.btn_2.setEnabled(False)
        self.thread_2 = PreventFastClickThreadSignal()
        self.thread_2._signal.connect(self.set_btn)
        self.thread_2.start()

    def set_btn(self):
        self.btn_2.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myshow = MyWin()
    myshow.show()
    sys.exit(app.exec_())