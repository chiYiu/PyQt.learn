# -*- coding: utf-8 -*-
import sys
from PySide.QtCore import Qt,QDate
from PySide.QtGui import QApplication, QWidget, QCalendarWidget,QVBoxLayout,\
                        QHBoxLayout,QLabel



#QCalendarWidget和QDateTimeEdit两个控件

EMOTION = {
    '周一':u'ヾ(≧▽≦*)o',
    '周二':u'φ(*￣0￣)',
    '周三':u'(≧▽≦q)',
    '周四':u'(｀∇´)ψ',
    '周五':u'（￣︶￣）↗',
    '周六':u'（￣︶￣）↗',
    '周日':u'[]~(￣▽￣)~*',}
class Demo(QWidget):
    """docstring for Demo"""
    def __init__(self):
        super(Demo, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowTitle('QCalendarWidget')

        self.calendar = QCalendarWidget(self)
        self.calendar.setMinimumDate(QDate(1946,2,14))
        self.calendar.setMaximumDate(QDate(6666,6,6))
        #self.calendar.setDateRange(QDate(1946,2,14),QDate(6666,6,6))
        #self.calendar.setFirstDayOfWeek(Qt.Monday)
        #self.calendar.setSelectedDate(QDate(1946,2,14))
        self.calendar.setGridVisible(True)
        self.calendar.clicked.connect(self.show_emotion_func)

        print(self.calendar.minimumDate())
        print(self.calendar.maximumDate())
        print(self.calendar.selectedDate())
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)

        weekday = self.calendar.selectedDate().toString('ddd')

        print(weekday)
        
        print(EMOTION['周一'])

        self.label.setText(EMOTION[weekday.encode('utf-8')])

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.calendar)
        self.v_layout.addWidget(self.label)

        self.setLayout(self.v_layout)

    def show_emotion_func(self):
        weekday = self.calendar.selectedDate().toString('ddd')
        self.label.setText(EMOTION[weekday.encode('utf-8')])

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())