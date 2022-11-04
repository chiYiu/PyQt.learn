## -*- coding: utf-8 -*-
#

#旧方法使用信号槽

# import sys
# from PySide.QtGui import QApplication, QPushButton

# from PySide.QtCore import SIGNAL, QObject

# def func():
#     print("func has been called!")

# app = QApplication(sys.argv)
# button = QPushButton("Call func")
# QObject.connect(button, SIGNAL ('clicked()'), func)
# button.show()                                                                                             

# sys.exit(app.exec_())



#改写后的新语法Signal()

# import sys
# from PySide.QtGui import QApplication, QPushButton

# def func():
#  print("func has been called!")

# app = QApplication(sys.argv)
# button = QPushButton("Call func")
# button.clicked.connect(func)
# button.show()
# sys.exit(app.exec_())


####在没有任何参数的情况下将信号连接到插槽


# import sys
# from PySide import QtCore, QtGui

# # define a function that will be used as a slot
# def sayHello():
#  print 'Hello world!'

# app = QtGui.QApplication(sys.argv)

# button = QtGui.QPushButton('Say hello!')

# # connect the clicked signal to the sayHello slot
# button.clicked.connect(sayHello)
# button.show()

# sys.exit(app.exec_())


#改写的将参数被添加到插槽并创建一个新信号

# import sys                                                                  
# from PySide.QtGui import QApplication, QPushButton                     
# from PySide.QtCore import QObject, Signal, Slot                            
                                                                            
# app = QApplication(sys.argv)                                                
                                                                            
# # define a new slot that receives a string and has                          
# # 'saySomeWords' as its name                                                
# @Slot(str)                                                                  
# def say_some_words(words):                                                  
#     print(words)                                                               
                                                                            
# class Communicate(QObject):                                                 
#  # create a new signal on the fly and name it 'speak'                       
#  speak = Signal(str)                                                        
                                                                            
# someone = Communicate()                                                     
# # connect signal and slot                                                   
# someone.speak.connect(say_some_words)                                         
# # emit 'speak' signal                                                         
# someone.speak.emit("Hello everybody!")

#使用装饰器重载

import sys                                                                  
from PySide.QtGui import QApplication, QPushButton                     
from PySide.QtCore import QObject, Signal, Slot                            
                                                                            
app = QApplication(sys.argv)                                                
                                                                            
# define a new slot that receives a C 'int' or a 'str'                      
# and has 'saySomething' as its name                                        
@Slot(int)                                                                  
@Slot(str)                                                                  
def say_something(stuff):                                                   
    print(stuff)                                                            
                                                                            
class Communicate(QObject):                                                 
    # create two new signals on the fly: one will handle                    
    # int type, the other will handle strings                               
    speak_number = Signal(int)                                              
    speak_word = Signal(str)                                                  
                                                                            
someone = Communicate()                                                     
# connect signal and slot properly                                          
someone.speak_number.connect(say_something)                                 
someone.speak_word.connect(say_something)                                   
# emit each 'speak' signal                                                  
someone.speak_number.emit(10)                                               
someone.speak_word.emit("Hello everybody!")