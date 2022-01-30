from pichess.square import Square

from PyQt6.QtWidgets import QWidget


class Board(QWidget):
    styles = 'pichess/assets/styles/board.css'

    def __init__(self, parent: QWidget) -> None:
        QWidget.__init__(self, parent)
        self.setObjectName('board')

        with open(self.styles) as f:
            self.setStyleSheet(f.read())

        self.set_squares()
        self.resize(800, 800)

    def set_squares(self) -> None:
        """create 64 (8x8) squares on the board"""

        for x in range(8):
            for y in range(8):
                Square(x, y, self)
    
    @property
    def squares(self) -> list[Square]:
        """return all squares of the board as a list"""

        return self.findChildren(Square)
