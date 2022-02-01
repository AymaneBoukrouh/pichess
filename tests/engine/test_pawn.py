from pichess.engine import Pawn
from unittest import TestCase


class TestPawn(TestCase):
    def test_possible_move_coordinates(self):
        # White Pawn
        self.assertEqual(
            Pawn('e2', True).possible_move_coordinates,
            {'e3', 'e4'}
        )

        self.assertEqual(
            Pawn('f4', True).possible_move_coordinates,
            {'f5'}
        )

        self.assertEqual(
            Pawn('a8', True).possible_move_coordinates,
            set()
        )

        self.assertEqual(
            Pawn('b7', True).possible_move_coordinates,
            {'b8'}
        )

        #Black Pawn
        self.assertEqual(
            Pawn('h7', False).possible_move_coordinates,
            {'h6', 'h5'}
        )

        self.assertEqual(
            Pawn('d3', False).possible_move_coordinates,
            {'d2'}
        )

        self.assertEqual(
            Pawn('c1', False).possible_move_coordinates,
            set()
        )

        self.assertEqual(
            Pawn('b2', False).possible_move_coordinates,
            {'b1'}
        )

    def test_possible_capture_coordinates(self):
        # White Pawn
        self.assertEqual(
            Pawn('a2', True).possible_capture_coordinates,
            {'b3'}
        )

        self.assertEqual(
            Pawn('d4', True).possible_capture_coordinates,
            {'c5', 'e5'}
        )

        self.assertEqual(
            Pawn('f8', True).possible,
            set()
        )

        # Black Pawn

        self.assertEqual(
            Pawn('h7', False).possible_capture_coordinates,
            {'g6'}
        )

        self.assertEqual(
            Pawn('f3', False).possible_capture_coordinates,
            {'e2', 'g2'}
        )

        self.assertEqual(
            Pawn('d8', False).possible_capture_coordinates,
            set()
        )
