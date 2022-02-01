from pichess.engine import Queen, Rook, Bishop
from unittest import TestCase


class TestQueen(TestCase):
    def test_possible_move_coordinates(self):
        for coordinates in ['f3', 'a1', 'b3', 'c8']:
            self.assertEqual(
                Queen(coordinates).possible_move_coordinates,
                {
                    *Bishop(coordinates).possible_move_coordinates,
                    *Rook(coordinates).possible_move_coordinates
                }
            )
