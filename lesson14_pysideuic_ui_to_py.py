##pysideuic

import sys, pprint
from pysideuic import compileUi
pyfile = open("D:/PyQt/designer.py", 'w')
compileUi("D:/PyQt/designer.ui", pyfile, False, 4, False)
pyfile.close()