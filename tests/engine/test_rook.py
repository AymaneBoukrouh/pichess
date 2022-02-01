from pichess.engine import Rook
from unittest import TestCase


class TestRook(TestCase):
    def test_possible_move_coordinates(self):
        self.assertEqual(
            Rook('h1').possible_move_coordinates,
            {
                'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', # files
                'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'  # ranks
            }
        )

        self.assertEqual(
            Rook('c4').possible_move_coordinates,
            {
                'a4', 'b4', 'd4', 'e4', 'f4', 'g4', 'h4', # files
                'c1', 'c2', 'c3', 'c5', 'c6', 'c7', 'c8'  # ranks
            }
        )

        self.assertEqual(
            Rook('f8').possible_move_coordinates,
            {
                'a8', 'b8', 'c8', 'd8', 'e8', 'g8', 'h8', # files
                'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7'  # ranks
            }
        )
