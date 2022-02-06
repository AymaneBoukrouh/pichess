#! /usr/bin/python

from pichess.ui.mainwindow import MainWindow
from PyQt6.QtWidgets import QApplication
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec())
