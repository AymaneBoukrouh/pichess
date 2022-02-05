from pichess.engine import Rook
from unittest import TestCase
from tests.engine.utils import load_fen


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

    def test_pseudolegal_coordinates(self):
        fen = load_fen('pseudolegal_coordinates')

        # coordinates, color, fen, pseudolegal_coordinates
        data = [
            ['d1', True, fen['1'], {'d2', 'd3','d4', 'd5', 'd6', 'e1', 'f1', 'g1'}],
            ['f1', True, fen['3'], {'a1', 'b1', 'c1', 'd1', 'e1', 'g1', 'h1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7'}],
            ['h1', True, fen['5'], set()],
            ['a1', True, fen['7'], {'b1', 'c1'}],
            ['f3', True, fen['9'], {'a3', 'b3', 'c3', 'd3', 'e3', 'f2'}],
            ['a3', False, fen['2'], {'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'a1', 'a2', 'a4', 'a5'}],
            ['h8', False, fen['4'], {'h5', 'h6', 'h7'}],
            ['c8', False, fen['6'], {'a8', 'b8', 'd3', 'e8', 'c5', 'c6', 'c7'}],
            ['a8', False, fen['8'], {'b7', 'c8', 'd8'}],
            ['g8', False, fen['10'], {'h7'}]
        ]

        for coordinates, color, fen, pseudolegal_coordinates in data:
            self.assertEqual(
                Rook(coordinates, color).pseudolegal_coordinates(fen),
                pseudolegal_coordinates
            )