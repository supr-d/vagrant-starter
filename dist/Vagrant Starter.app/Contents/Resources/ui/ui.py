# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../../../../../../../testPyQt4/app.ui'
#
# Created: Thu May 14 01:12:57 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(593, 359)
        MainWindow.setMinimumSize(QtCore.QSize(593, 359))
        MainWindow.setMaximumSize(QtCore.QSize(593, 359))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.buttonGetPaths = QtGui.QPushButton(self.centralwidget)
        self.buttonGetPaths.setGeometry(QtCore.QRect(440, 20, 141, 32))
        self.buttonGetPaths.setStyleSheet(_fromUtf8(""))
        self.buttonGetPaths.setObjectName(_fromUtf8("buttonGetPaths"))
        self.comboPaths = QtGui.QComboBox(self.centralwidget)
        self.comboPaths.setGeometry(QtCore.QRect(10, 20, 421, 31))
        self.comboPaths.setStyleSheet(_fromUtf8("font-size: 14pt;"))
        self.comboPaths.setObjectName(_fromUtf8("comboPaths"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 571, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.buttonUp = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.buttonUp.setStyleSheet(_fromUtf8(""))
        self.buttonUp.setObjectName(_fromUtf8("buttonUp"))
        self.horizontalLayout.addWidget(self.buttonUp)
        self.buttonSuspend = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.buttonSuspend.setObjectName(_fromUtf8("buttonSuspend"))
        self.horizontalLayout.addWidget(self.buttonSuspend)
        self.buttonReload = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.buttonReload.setObjectName(_fromUtf8("buttonReload"))
        self.horizontalLayout.addWidget(self.buttonReload)
        self.buttonHalt = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.buttonHalt.setObjectName(_fromUtf8("buttonHalt"))
        self.horizontalLayout.addWidget(self.buttonHalt)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 110, 571, 241))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.buttonGetPaths.setText(_translate("MainWindow", "refresh", None))
        self.buttonUp.setText(_translate("MainWindow", "up", None))
        self.buttonSuspend.setText(_translate("MainWindow", "suspend", None))
        self.buttonReload.setText(_translate("MainWindow", "reload", None))
        self.buttonHalt.setText(_translate("MainWindow", "halt", None))

