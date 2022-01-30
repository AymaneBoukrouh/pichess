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
    def from_letter(letter, coordinates, parent, shadow=False) -> Piece:
        """initiate piece from letter, returns appropriate piece object"""

        color = ('A' <= letter <= 'Z') # True -> white, False -> black

        match letter:
            case 'K' | 'k': PieceType = King
            case 'Q' | 'q': PieceType = Queen
            case 'R' | 'r': PieceType = Rook
            case 'B' | 'b': PieceType = Bishop
            case 'N' | 'n': PieceType = Knight
            case 'P' | 'p': PieceType = Pawn

        return PieceType(coordinates, color, parent, shadow)

    def set_coordinates(self, coordinates: str) -> None:
        """set coordinates and move piece to the appropriate square"""

        self.setObjectName(coordinates)
        self.coordinates = coordinates

        square = self.board.get_square_by_coordinates(coordinates)
        x, y = map(int, (square.x(), square.y()))
        self.move(x, y)

    
    def mousePressEvent(self, event):
        """move the clicked piece right under the mouse cusor and create shadow"""

        self.move_under_mouse(event)
        self.show_shadow() # dislay a shadow to mark original position when moving the piece
        self.appear_on_top() # not allow any piece to appear on top of current piece
        self.highlight_move()

    def mouseMoveEvent(self, event):
        """keep the clicked piece right under the mouse cursor"""

        self.move_under_mouse(event)
        self.highlight_move()
    
    def mouseReleaseEvent(self, event):
        """change position of piece if it is valid and hide shadow"""

        self.set_coordinates(self.current_coordinates)
        self.hide_shadow()
        self.highlighted_square.clear_highlight()

    def move_under_mouse(self, event) -> None:
        """move piece right under the mouse cursor"""

        mouse_pos = self.mapTo(self.board, event.position())
        x, y = map(int, (mouse_pos.x(), mouse_pos.y()))

        board_width = board_height = self.board.size().width()
        if not (0<x<board_width and 0<y<board_height):
            return # don't move piece if coordinates are outside the board

        width = height = self.size().width()
        center_x, center_y = x-width//2, y-height//2 # to make the center of the piece under the cursor
        self.move(center_x, center_y)


    def make_shadow(self) -> None:
        """add transparency effect to the piece"""

        opacity = QGraphicsOpacityEffect()
        opacity.setOpacity(.3)
        self.setGraphicsEffect(opacity)
    
    def show_shadow(self) -> None:
        """create a shadow piece of same type in the square with current coordinates of the piece"""

        self.shadow = Piece.from_letter(
            self.letter,
            self.coordinates,
            parent = self.board,
            shadow = True
        )

        self.shadow.stackUnder(self) # make current piece on top of shadow, not the opposite
        self.shadow.show()
    
    def hide_shadow(self) -> None:
        """destroy shadow piece"""

        self.shadow.setParent(None)
        del self.shadow

    def highlight_move(self) -> None:
        """highlight the square that the piece in on"""

        try:
            self.highlighted_square.clear_highlight()
        except AttributeError:
            pass # if no square is highlighted then ignore

        self.current_square.display_highlight('darkgreen')
        self.highlighted_square = self.current_square

    def appear_on_top(self) -> None:
        """make all pieces stacked under current piece"""

        for piece in self.board.pieces:
            if piece is not self:
                piece.stackUnder(self)

    @property
    def current_coordinates(self) -> str:
        """calculate coordinates from current position"""

        pos = self.pos()
        width = height = self.size().width()
        x = (pos.x() + width//2) // width
        y = (pos.y() + width//2) // height

        file = chr(ord('a') + x)
        rank = 8-y

        return f'{file}{rank}'

    @property
    def current_square(self) -> Square:
        """get square from current coordinates"""

        return self.board.get_square_by_coordinates(self.current_coordinates)


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
