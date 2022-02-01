from pichess.engine import Knight
from unittest import TestCase


class TestKnight(TestCase):
    def test_possible_move_coordinates(self):
        self.assertEqual(
            Knight('g8').possible_move_coordinates,
            {'e7', 'f6', 'h6'}
        )

        self.assertEqual(
            Knight('d4').possible_move_coordinates,
            {'b3', 'b5', 'c2', 'c6', 'e2', 'e6', 'f3', 'f5'}
        )

        self.assertEqual(
            Knight('h1').possible_move_coordinates,
            {'f2', 'g3'}
        )
