# -*- coding: utf-8 -*-
####事件处理####
##窗口关闭事件
import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication, QWidget, QTextEdit,QPushButton,\
                        QVBoxLayout,QHBoxLayout,QMessageBox

class Demo(QWidget):
    """docstring for Demo"""
    def __init__(self):
        super(Demo, self).__init__()
        
        self.is_save = True
        # is_saved变量用于记录用户是否已经进行保存；

        self.textedit = QTextEdit(self)
        self.textedit.textChanged.connect(self.on_textchanged_func)
        #实例化一个QTextEdit控件用于文本编辑，将其textChanged信号和自定义的槽函数连接起来

        self.button = QPushButton(self)
        self.button.clicked.connect(self.on_clicked_func)
        #实例化一个按钮用于保存操作，将clicked信号与自定义的槽函数进行连接

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.textedit)
        self.v_layout.addWidget(self.button)
        self.setLayout(self.v_layout)

    def on_textchanged_func(self):
        if self.textedit.toPlainText():
            self.is_save = False
        else:
            self.is_save = True


    def on_clicked_func(self):
        self.save_func(self.textedit.toPlainText())
        self.is_save = True

    def save_func(self,text):
        with open('save.txt','w')as f:
            f.write(text)

    def closeEvent(self,QcloseEvent):
        if not self.is_save:
            choice = QMessageBox.question(self,'','Do yout want to save the text?',
                                            QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
            if choice == QMessageBox.Yes:
                self.save_func(self.textedit.toPlainText())
                QcloseEvent.accept()
            elif choice == QMessageBox.No:
                QcloseEvent.accept()
            else:
                QcloseEvent.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())