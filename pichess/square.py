from PyQt6.QtWidgets import QWidget, QFrame, QLabel, QGraphicsOpacityEffect
from PyQt6.QtCore import QRect, Qt


class Square(QFrame):
    def __init__(self, x, y, parent: QWidget) -> None:
        QFrame.__init__(self, parent)

        file = chr(ord('a') + x) # vertical columns, labeled a through h
        rank = 8-y # horizontal rows, numbered 1 to 8, starting from white (bottom)
        self.coordinates = f'{file}{rank}'

        self.setObjectName(self.coordinates)
        self.setGeometry(QRect(x*100, y*100, 100, 100))
        self.set_color(x, y) # set square color depending on coordinates

        self.dot_setup()
        self.corner_setup()
        self.highlight_setup()
        self.coordinates_label_setup()

    def set_color(self, x, y) -> None:
        """set square color depending on coordinates"""

        if x%2 == y%2:
            self.setProperty('color', 'light-square')

        else:
            self.setProperty('color', 'dark-square')

    def dot_setup(self) -> None:
        """create dot object to display a dot on top of square"""

        dot = QFrame(self)
        dot.setGeometry(QRect(35, 35, 100-35*2, 100-35*2))
        dot.setProperty('type', 'dot') # for styling using css (styles: board.css)
        dot.setVisible(False)
        self.dot = dot

    def display_dot(self, value: bool) -> None:
        """hide/show dot on top on square"""

        self.dot.setVisible(value)

    def corner_setup(self) -> None:
        """create corner object to display a corner around square"""

        corner = QFrame(self)
        corner.setGeometry(QRect(-20, -20, 100+20*2, 100+20*2))
        corner.setProperty('type', 'corner') # for styling using css (styles: board.css)
        corner.setVisible(False)
        self.corner = corner

    def display_corner(self, value: bool) -> None:
        """hide/show corner around square"""

        self.corner.setVisible(value)

    def highlight_setup(self) -> None:
        """create highlight object to display a semi-transparent background color"""

        opacity = QGraphicsOpacityEffect()
        opacity.setOpacity(.3)

        highlight = QFrame(self)
        highlight.setGeometry(QRect(0, 0, 100, 100))
        highlight.setGraphicsEffect(opacity)
        highlight.setVisible(False)
        self.highlight = highlight

    def display_highlight(self, color: str) -> None:
        """add semi-transparent background color to square"""

        self.highlight.setStyleSheet(f'background-color: {color}')
        self.highlight.setVisible(True)

    def clear_highlight(self) -> None:
        """remove semi-trasparent background color from square"""

        self.highlight.setVisible(False)

    def coordinates_label_setup(self) -> None:
        """create coordinates object to display coordinates on top of square"""

        coordinates_label = QLabel(self.coordinates, self)
        coordinates_label.setGeometry(QRect(0, 0, 100, 100))
        coordinates_label.setProperty('type', 'coordinates') # for styling using css (styles: board.css)
        coordinates_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        coordinates_label.setVisible(False)
        self.coordinates_label = coordinates_label

    def display_coordinates(self, value: bool) -> None:
        """hide/show coordinates on top of square"""

        self.coordinates_label.setVisible(value)
