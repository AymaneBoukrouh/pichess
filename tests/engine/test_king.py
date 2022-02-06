from tests.engine.utils import load_fen
from pichess.engine.pieces import King
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

    def test_pseudolegal_coordinates(self):
        fen = load_fen('pseudolegal_coordinates')

        # white
        self.assertEqual(
            King('c1', True).pseudolegal_coordinates(fen['1']),
            {'b1', 'd2'}
        )

        self.assertEqual(
            King('e3', True).pseudolegal_coordinates(fen['3']),
            {'d2', 'd3', 'e2', 'e4', 'f2', 'f3', 'f4'}
        )

        self.assertEqual(
            King('e1', True).pseudolegal_coordinates(fen['5']),
            {'d2', 'e2', 'f1'}
        )

        self.assertEqual(
            King('g1', True).pseudolegal_coordinates(fen['7']),
            {'h1', 'h2'}
        )

        self.assertEqual(
            King('h2', True).pseudolegal_coordinates(fen['9']),
            {'g1', 'g3', 'h1'}
        )

        #black
        self.assertEqual(
            King('g8', False).pseudolegal_coordinates(fen['2']),
            {'f7', 'f8', 'h7', 'h8'}
        )

        self.assertEqual(
            King('e8', False).pseudolegal_coordinates(fen['4']),
            {'d7', 'd8', 'e7'}
        )

        self.assertEqual(
            King('h8', False).pseudolegal_coordinates(fen['6']),
            {'g8', 'h7'}
        )

        self.assertEqual(
            King('e8', False).pseudolegal_coordinates(fen['8']),
            {'d7', 'd8', 'e7'}
        )

        self.assertEqual(
            King('e8', False).pseudolegal_coordinates(fen['10']),
            {'d7', 'd8'}
        )
