from pichess.engine import Bishop
from unittest import TestCase
from tests.engine.utils import load_fen


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

    def test_pseudolegal_coordinates(self):
        fen = load_fen('pseudolegal_coordinates')

        # coordinates, color, fen, pseudolegal_coordinates
        data = [
            #['f2', True, fen['1'], {'a7', 'b6', 'c5', 'd4', 'e1', 'e3', 'g1', 'g3'}],
            #['b5', True, fen['5'], {'a4', 'a6', 'c4', 'c6', 'd3', 'd7', 'e2', 'f1'}],
            ['d3', True, fen['7'], {'a6', 'b1', 'b5', 'c2', 'c4', 'e2', 'e4', 'f5', 'g6', 'h7'}],
            ['e5', False, fen['2'], {'a1', 'b2', 'b8', 'c3', 'c7', 'd4', 'd6', 'f4', 'f6', 'g3'}],
            ['f8', False, fen['4'], {'e7'}],
            ['f8', False, fen['8'], {'a3', 'b4', 'c5', 'd6', 'e7'}],
            ['f8', False, fen['10'], set()]
        ]

        for coordinates, color, fen, pseudolegal_coordinates in data:
            self.assertEqual(
                Bishop(coordinates, color).pseudolegal_coordinates(fen),
                pseudolegal_coordinates
            )
