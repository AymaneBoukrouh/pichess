from pichess.engine import Queen, Rook, Bishop
from unittest import TestCase
from tests.engine.utils import load_fen


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

    def test_pseudolegal_coordinates(self):
        fen = load_fen('pseudolegal_coordinates')

        # white
        self.assertEqual(
            Queen('g8', True).pseudolegal_coordinates(fen['1']),
            {'e6', 'f7', 'f8', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'h7', 'h8'}
        )

        self.assertEqual(
            Queen('d1', True).pseudolegal_coordinates(fen['5']),
            {'a4', 'b3', 'c2', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'e2', 'f3', 'g4', 'h5'}
        )

        self.assertEqual(
            Queen('d1', True).pseudolegal_coordinates(fen['7']),
            {'a4', 'b1', 'b3', 'c1', 'c2', 'd2', 'e1', 'e2'}
        )

        self.assertEqual(
            Queen('b2', True).pseudolegal_coordinates(fen['9']),
            {'a1', 'a3', 'b1', 'b3', 'b4', 'b5', 'b6', 'b7', 'c2', 'c3', 'd2', 'e2', 'f2'}
        )

        # black
        self.assertEqual(
            Queen('h4', False).pseudolegal_coordinates(fen['4']),
            {'d8', 'e1', 'e7', 'f2', 'f6', 'g3', 'g5', 'h1', 'h2', 'h3', 'h5', 'h6', 'h7'}
        )

        self.assertEqual(
            Queen('d2', False).pseudolegal_coordinates(fen['6']),
            {'a2', 'a5', 'b2', 'b4', 'c1', 'c2', 'c3', 'd1', 'd3', 'd4', 'e1', 'e2', 'e3', 'f2', 'g2'}
        )

        self.assertEqual(
            Queen('e4', False).pseudolegal_coordinates(fen['8']),
            {'a4', 'b1', 'b4', 'c2', 'c4', 'd3', 'd4', 'd5', 'e3', 'e5', 'f3', 'f4', 'f5', 'g2', 'g4', 'g6', 'h1', 'h4'}
        )

        self.assertEqual(
            Queen('b4', False).pseudolegal_coordinates(fen['10']),
            {'a3', 'a4', 'a5', 'b2', 'b3', 'b5', 'c3', 'c4', 'c5', 'd2', 'd4', 'd6'}
        )
