from pichess.ui.square import Square
from pichess.ui.pieces import Piece
from pichess.utils import fen_to_matrix
from PyQt6.QtWidgets import QWidget


class Board(QWidget):
    styles = 'pichess/ui/assets/styles/board.css'

    def __init__(self, parent: QWidget) -> None:
        QWidget.__init__(self, parent)
        self.setObjectName('board')

        with open(self.styles) as f:
            self.setStyleSheet(f.read())

        self.set_squares()
        self.resize(800, 800)

        self.set_fen_position('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')

    def set_squares(self) -> None:
        '''create 64 (8x8) squares on the board'''

        for x in range(8):
            for y in range(8):
                Square(x, y, self)

    def set_fen_position(self, fen: str) -> None:
        '''set position from fen string'''

        for piece in self.pieces:
            piece.setParent(None)
            del piece
    
        matrix = fen_to_matrix(fen)
        for coordinates in matrix:
            piece_letter = matrix[coordinates]
            if piece_letter:
                piece = Piece.from_letter(piece_letter, coordinates, self)
                piece.show()

    @property
    def pieces(self) -> list[Piece]:
        '''return all pieces on the board as a list'''

        return self.findChildren(Piece)

    def get_piece_by_coordinates(self, coordinates: str) -> Piece:
        '''return piece with specified coordinates'''

        return self.findChild(Piece, coordinates)
    
    @property
    def squares(self) -> list[Square]:
        '''return all squares of the board as a list'''

        return self.findChildren(Square)

    def get_square_by_coordinates(self, coordinates: str) -> Square:
        '''return square with specified coordinates'''

        return self.findChild(Square, coordinates)