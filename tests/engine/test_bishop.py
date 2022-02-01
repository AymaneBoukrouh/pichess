from pichess.engine import Bishop
from unittest import TestCase


class TestBishop(TestCase):
    def test_possible_move_coordinates(self):
        self.assertEqual(
            Bishop('f5').possible_move_coordinates,
            {
                'c8', 'd7', 'e6', 'g4', 'h3',            # \ diagonal
                'b1', 'c2', 'd3', 'e4', 'g6', 'h7'       # / diagonal
            }
        )

        self.assertEqual(
            Bishop('c1').possible_move_coordinates,
            {
                'a3', 'b2',                              # \ diagonal
                'd2', 'e3', 'f4', 'g5', 'h6'             # / diagonal
            }
        )

        self.assertEqual(
            Bishop('a8').possible_move_coordinates,
            {
                'b7', 'c6', 'd5', 'e4', 'f3', 'g2', 'h1' # \ diagonal
            }
        )
