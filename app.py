# -*- coding: utf-8 -*-

import json
from PyQt4 import uic
from PyQt4.QtCore import Qt, SIGNAL
from PyQt4.QtGui import QApplication, QTextCursor
from workers import VagrantCommand, VagrantPaths

Ui_MainWindow, QMainWindow = uic.loadUiType('ui/app.ui')


def readPathsFromCache():
    try:
        with open('paths.json') as paths_file:
            return json.load(paths_file)
    except Exception:
        pass

def writePathsToCache(data):
    with open('paths.json', 'w') as paths_file:
        paths_file.write(data)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # убрать кнопку расширения окна
        self.setWindowFlags(Qt.WindowMaximizeButtonHint)
        # отключить возможность редактирования текстового поля
        self.ui.textEdit.setReadOnly(True)

        vagrantPaths = readPathsFromCache()

        if vagrantPaths is not None:
            self.refreshPaths = False
            self.addPaths(vagrantPaths)
        else:
            self.refreshPaths = True

        self.vagrantPaths = VagrantPaths()
        self.vagrantCommand = VagrantCommand()

        self.connectSignals()

    def __del__(self):
        self.ui = None

    def connectSignals(self):
        self.connect(
            self.vagrantPaths,
            SIGNAL('paths(QStringList)'),
            self.addPaths,
            Qt.QueuedConnection
        )

        self.connect(
            self.vagrantCommand,
            SIGNAL('commandOutput(QString)'),
            self.printString,
            Qt.QueuedConnection
        )

        self.connect(
            self.vagrantCommand,
            SIGNAL('commandFinish()'),
            self.enableCommandButtons,
            Qt.QueuedConnection
        )

        self.ui.buttonGetPaths.clicked.connect(self.getPaths)
        self.ui.buttonUp.clicked.connect(lambda: self.runCommand('up'))
        self.ui.buttonSuspend.clicked.connect(lambda: self.runCommand('suspend'))
        self.ui.buttonReload.clicked.connect(lambda: self.runCommand('reload'))
        self.ui.buttonHalt.clicked.connect(lambda: self.runCommand('halt'))

    def runCommand(self, action):
        self.setCursor(Qt.BusyCursor)
        self.disableCommandButtons()
        self.vagrantCommand.path = self.getCurrentPath()
        self.vagrantCommand.action = action
        self.vagrantCommand.start()

    def disableCommandButtons(self):
        self.ui.buttonUp.setDisabled(True)
        self.ui.buttonSuspend.setDisabled(True)
        self.ui.buttonReload.setDisabled(True)
        self.ui.buttonHalt.setDisabled(True)

    def enableCommandButtons(self):
        self.ui.buttonUp.setDisabled(False)
        self.ui.buttonSuspend.setDisabled(False)
        self.ui.buttonReload.setDisabled(False)
        self.ui.buttonHalt.setDisabled(False)
        self.unsetCursor()

    def getCurrentPath(self):
        return self.ui.comboPaths.currentText()

    def printString(self, string):
        self.ui.textEdit.append(string)
        # автопрокрутка списка
        self.ui.textEdit.moveCursor(QTextCursor.End)

    def getPaths(self):
        self.setCursor(Qt.BusyCursor)
        self.ui.buttonGetPaths.setDisabled(True)
        self.vagrantPaths.start()

    def addPaths(self, paths):
        self.ui.comboPaths.clear()

        if self.refreshPaths:
            writePathsToCache(json.dumps(paths))

        for path in paths:
            self.ui.comboPaths.addItem(path)

        self.unsetCursor()
        self.ui.buttonGetPaths.setDisabled(False)


if __name__ == '__main__':
    import sys

    application = QApplication(sys.argv)
    application.setApplicationName('Vagrant Starter')

    mainWindow = MainWindow()
    mainWindow.setWindowTitle('Vagrant Starter')
    mainWindow.show()

    sys.exit(application.exec_())