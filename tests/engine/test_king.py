from pichess.engine import King
from unittest import TestCase


class TestKing(TestCase):
    def test_possible_move_coordinates(self):
        self.assertEqual(
            King('a1').possible_move_coordinates,
            {'a2', 'b1', 'b2'}
        )

        self.assertEqual(
            King('e4').possible_move_coordinates,
            {'e5', 'f5', 'f4', 'f3', 'e3', 'd3', 'd4', 'd5'}
        )

        self.assertEqual(
            King('d8').possible_move_coordinates,
            {'e8', 'e7', 'd7', 'c7', 'c8'}
        )
