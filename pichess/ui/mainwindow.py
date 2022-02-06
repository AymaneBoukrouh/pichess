from pichess.ui.board import Board
from PyQt6.QtWidgets import QMainWindow, QWidget, QGridLayout


class MainWindow(QMainWindow):
    styles = 'pichess/ui/assets/styles/mainwindow.css'

    def __init__(self) -> None:
        QMainWindow.__init__(self)
        self.setWindowTitle('pichess')

        with open(self.styles) as f:
            self.setStyleSheet(f.read())

        centralWidget = CentralWidget(self)
        self.setCentralWidget(centralWidget)

        self.showMaximized()


class CentralWidget(QWidget):
    def __init__(self, parent: QMainWindow) -> None:
        QWidget.__init__(self, parent)

        self.layout = QGridLayout(self)
        self.layout.setSpacing(0)

        self.board = Board(self)
        self.board.setFixedSize(
            self.board.width(),
            self.board.height()
        )

        self.layout.addWidget(self.board)
