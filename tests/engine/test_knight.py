from pichess.engine import Knight
from unittest import TestCase
from tests.engine.utils import load_fen


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

    def test_pseudolegal_coordinates(self):
        fen = load_fen('pseudolegal_coordinates')

        # coordinates, color, fen, pseudolegal_coordinates
        data = [
            ['c3', True, fen['1'], {'a2', 'a4', 'b1', 'b5', 'd5', 'e2'}],
            ['c3', True, fen['5'], {'a4', 'b1', 'd5', 'e2'}],
            ['f3', True, fen['7'], {'d2', 'd4', 'e1', 'e5', 'h2', 'g4'}],
            ['f1', True, fen['9'], {'d2', 'e3', 'g3'}],
            ['g8', False, fen['4'], {'e7', 'f6', 'h6'}],
            ['f4', False, fen['6'], {'d3', 'd5', 'e2', 'e6', 'g2', 'g6', 'h3', 'h5'}],
            ['g8', False, fen['8'], {'e7', 'f6', 'h6'}],
            ['g8', False, fen['10'], {'f6'}],
            ['c6', False, fen['10'], {'a5', 'b8', 'd4', 'd8', 'e5'}]
        ]

        for coordinates, color, fen, pseudolegal_coordinates in data:
            self.assertEqual(
                Knight(coordinates, color).pseudolegal_coordinates(fen),
                pseudolegal_coordinates
            )
