# -*- coding: utf-8 -*-
import sys
from PySide.QtCore import Qt,QDate,QTime,QDateTime
from PySide.QtGui import QApplication, QWidget, QDateTimeEdit,QDateEdit,QTimeEdit,\
                        QVBoxLayout

#QDateTimeEdit是QDateEdit和QTimeEdit的父类，看名字就知道QDateTimeEdit可以编辑日期和时间，
#QDateEdit只能编辑日期(年月日)，而QTimeEdit只能编辑时间(时分秒)，

class Demo(QWidget):
    """docstring for Demo"""
    def __init__(self):
        super(Demo, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowTitle('QDateTimeEdit')
        self.datetime_1 = QDateTimeEdit(self)
        self.datetime_1.dateChanged.connect(lambda: self.print_func('Date Changed!'))

        self.datetime_2 = QDateTimeEdit(QDateTime.currentDateTime(),self)
        self.datetime_2.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        self.datetime_2.timeChanged.connect(lambda: self.print_func('Time Changed!'))
        print(self.datetime_2.date())
        print(self.datetime_2.time())
        print(self.datetime_2.dateTime())

        self.datetime_3 = QDateTimeEdit(QDateTime.currentDateTime(),self)
        self.datetime_3.dateTimeChanged.connect(lambda: self.print_func('DateTime Changed!'))
        self.datetime_3.setCalendarPopup(True)

        self.datetime_4 = QDateTimeEdit(QDate.currentDate(),self)
        self.datetime_5 = QDateTimeEdit(QTime.currentTime(),self)

        self.date = QDateEdit(QDate.currentDate(),self)
        self.date.setDisplayFormat('yyyy/MM/dd')
        print(self.date.date())

        self.time = QTimeEdit(QTime.currentTime(),self)
        self.time.setDisplayFormat('HH:mm:ss')
        print(self.time.time())

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.datetime_1)
        self.v_layout.addWidget(self.datetime_2)
        self.v_layout.addWidget(self.datetime_3)
        self.v_layout.addWidget(self.datetime_4)
        self.v_layout.addWidget(self.datetime_5)
        self.v_layout.addWidget(self.date)
        self.v_layout.addWidget(self.time)

        self.setLayout(self.v_layout)

    def print_func(self,output):
        print output

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())