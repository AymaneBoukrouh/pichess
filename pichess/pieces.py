from __future__ import annotations
from PyQt6.QtWidgets import QWidget, QGraphicsOpacityEffect
from PyQt6.QtSvgWidgets import QSvgWidget


class Piece(QSvgWidget):
    def __init__(self, coordinates, color, parent, shadow=False):
        QSvgWidget.__init__(self, parent)
        self.color = color
        self.parent = self.board = parent

        self.setStyleSheet('background-color: none')
        self.resize(100, 100)

        self.set_coordinates(coordinates)
        self.load(f'pichess/assets/svg/pieces/{self.letter}.svg')

        if shadow:
            self.make_shadow()

    @staticmethod
    def from_letter(letter, coordinates, parent) -> Piece:
        """initiate piece from letter, returns appropriate piece object"""

        color = ('A' <= letter <= 'Z') # True -> white, False -> black

        match letter:
            case 'K' | 'k': PieceType = King
            case 'Q' | 'q': PieceType = Queen
            case 'R' | 'r': PieceType = Rook
            case 'B' | 'b': PieceType = Bishop
            case 'N' | 'n': PieceType = Knight
            case 'P' | 'p': PieceType = Pawn

        return PieceType(coordinates, color, parent)

    def set_coordinates(self, coordinates: str) -> None:
        """set coordinates and move piece to the appropriate square"""

        self.setObjectName(coordinates)
        self.coordinates = coordinates

        square = self.board.get_square_by_coordinates(coordinates)
        x, y = map(int, (square.x(), square.y()))
        self.move(x, y)

    def make_shadow(self) -> None:
        """add transparency effect to the piece"""

        opacity = QGraphicsOpacityEffect()
        opacity.setOpacity(.3)
        self.setGraphicsEffect(opacity)


class King(Piece):
    def __init__(self, coordinates, color, parent, shadow=False):
        self.letter = 'K' if color else 'k'

        Piece.__init__(self, coordinates, color, parent, shadow)
        self.setProperty('name', 'king')


class Queen(Piece):
    def __init__(self, coordinates, color, parent, shadow=False):
        self.letter = 'Q' if color else 'q'
    
        Piece.__init__(self, coordinates, color, parent, shadow)
        self.setProperty('name', 'queen')


class Rook(Piece):
    def __init__(self, coordinates, color, parent, shadow=False):
        self.letter = 'R' if color else 'r'

        Piece.__init__(self, coordinates, color, parent, shadow)
        self.setProperty('name', 'rook')


class Bishop(Piece):
    def __init__(self, coordinates, color, parent, shadow=False):
        self.letter = 'B' if color else 'b'

        Piece.__init__(self, coordinates, color, parent, shadow)
        self.setProperty('name', 'bishop')


class Knight(Piece):
    def __init__(self, coordinates, color, parent, shadow=False):
        self.letter = 'N' if color else 'n'

        Piece.__init__(self, coordinates, color, parent, shadow)
        self.setProperty('name', 'knight')
    

class Pawn(Piece):
    def __init__(self, coordinates, color, parent, shadow=False):
        self.letter = 'P' if color else 'p'

        Piece.__init__(self, coordinates, color, parent, shadow)
        self.setProperty('name', 'pawn')
