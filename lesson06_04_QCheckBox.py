# -*- coding: utf-8 -*-
import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication,QWidget,QCheckBox,QVBoxLayout

#QCheckBox 该控件为复选框，即可以进行多选操作
class Demo(QWidget):
	"""docstring for Demo"""
	def __init__(self):
		super(Demo, self).__init__()
		self.checkbox1 = QCheckBox('Checkbox1',self)
		self.checkbox2 = QCheckBox('Checkbox2',self)
		self.checkbox3 = QCheckBox('Checkbox3',self)

		self.v_layout = QVBoxLayout()

		self.layout_init()
		self.checkbox_init()

	def layout_init(self):
		self.v_layout.addWidget(self.checkbox1)
		self.v_layout.addWidget(self.checkbox2)
		self.v_layout.addWidget(self.checkbox3)

		self.setLayout(self.v_layout)

	def checkbox_init(self):
		self.checkbox1.setChecked(True)															#1
		#self.checkbox1.setCheckState(QT.Checked)												#2
		self.checkbox1.stateChanged.connect(lambda: self.on_state_change_func(self.checkbox1))	#3

		self.checkbox2.setChecked(True)
		#self.checkbox2.setCheckState(QT.Checked)
		self.checkbox2.stateChanged.connect(lambda: self.on_state_change_func(self.checkbox2))

		self.checkbox3.setTristate(True)														#4
		self.checkbox3.setCheckState(Qt.PartiallyChecked)										#5
		self.checkbox2.stateChanged.connect(lambda: self.on_state_change_func(self.checkbox3))	#6

	def on_state_change_func(self,checkbox):
		print('{} was cliked, and its current state is {}'.format(checkbox.text(),checkbox.checkState()))
		
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec_())

#1.2 通过setChecked()方法传入True或者False可以将复选框设为选中或无选中状态；
#另外一种替代的方法是setCheckState()，传入的参数可以是选中状态Qt.Checked,
#无选中状态Qt.Unchecked和半选中状态Qt.PartiallyChecked；

#3 stateChanged信号会在复选框状态发生改变的时候发出。这里我们发现槽函数是带参数的，
# 可以通过lambda表达式来将参数传入槽函数。
# 若单纯使用self.on_state_change_func(self.checkbox2)则会报错；

#4 5 如果要让一个复选框拥有三种状态，则必须通过setTristate(True)方法来实现。
#在这里我们让第三个复选框拥有三种状态

#6 checkState()方法可以获取当前复选框的状态，返回值为int类型，
#  0为无选中状态，1为半选中状态，2位选中状态。