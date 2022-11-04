# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/PyQt/designer.ui'
#
# Created: Wed Apr 27 15:20:45 2022
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(536, 228)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.edit_label = QtGui.QLabel(Form)
        self.edit_label.setObjectName("edit_label")
        self.gridLayout.addWidget(self.edit_label, 0, 0, 1, 1)
        self.browser_label = QtGui.QLabel(Form)
        self.browser_label.setObjectName("browser_label")
        self.gridLayout.addWidget(self.browser_label, 0, 1, 1, 1)
        self.text_edit = QtGui.QTextBrowser(Form)
        self.text_edit.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.text_edit.setReadOnly(False)
        self.text_edit.setOverwriteMode(True)
        self.text_edit.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.text_edit.setObjectName("text_edit")
        self.gridLayout.addWidget(self.text_edit, 1, 0, 1, 1)
        self.text_browser = QtGui.QTextBrowser(Form)
        self.text_browser.setReadOnly(True)
        self.text_browser.setObjectName("text_browser")
        self.gridLayout.addWidget(self.text_browser, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.edit_label.setText(QtGui.QApplication.translate("Form", "QTextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.browser_label.setText(QtGui.QApplication.translate("Form", "QTextBrowser", None, QtGui.QApplication.UnicodeUTF8))

