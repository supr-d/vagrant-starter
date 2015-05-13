# -*- coding: utf-8 -*-

import subprocess
from PyQt4.QtCore import QThread, SIGNAL


class VagrantPaths(QThread):
    def __init__(self, parent=None):
        QThread.__init__(self, parent)

    def run(self):
        output = subprocess.Popen(
            "vagrant global-status --prune | awk '{ print $5 }' | grep '^\/'",
            shell=True,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE
        ).stdout

        paths = [line.decode('utf-8').strip() for line in output]

        self.emit(SIGNAL('paths(QStringList)'), paths)


class VagrantCommand(QThread):
    commandTemplate = 'cd %s && vagrant %s'

    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.action = None
        self.path = None

    def _getCommand(self):
        return self.commandTemplate % (self.path, self.action)

    def run(self):
        output = subprocess.Popen(
            self._getCommand(),
            shell=True,
            stdout=subprocess.PIPE
        )

        while True:
            line = output.stdout.readline()

            if line:
                self.emit(SIGNAL('commandOutput(QString)'), line.decode('utf-8').rstrip())
            else:
                self.emit(SIGNAL('commandFinish()'))
                break
