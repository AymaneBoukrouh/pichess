from tests.engine.utils import load_fen
from pichess.engine.engine import Engine
from unittest import TestCase


class TestEngine(TestCase):
    def setUp(self):
        self.engine = Engine()

    def test_is_check(self):
        # is_check
        fen = load_fen('is_check')

        self.engine.set_fen_position(fen['1'])
        self.assertTrue(self.engine.is_check)

        self.engine.set_fen_position(fen['2'])
        self.assertTrue(self.engine.is_check)

        # is_not_check
        fen = load_fen('is_not_check')

        self.engine.set_fen_position(fen['1'])
        self.assertFalse(self.engine.is_check)

    def test_is_checkmate(self):
        fen = load_fen('is_checkmate')

        self.engine.set_fen_position(fen['1'])
        self.assertTrue(self.engine.is_checkmate)

        self.engine.set_fen_position(fen['2'])
        self.assertTrue(self.engine.is_checkmate)

    def test_is_draw(self):
        fen = load_fen('is_draw')

        self.engine.set_fen_position(fen['1'])
        self.assertTrue(self.engine.is_draw)

        self.engine.set_fen_position(fen['2'])
        self.assertTrue(self.engine.is_draw)

        self.engine.set_fen_position(fen['3'])
        self.assertTrue(self.engine.is_draw)

    def test_is_stalemate(self):
        fen = load_fen('is_stalemate')

        self.engine.set_fen_position(fen['1'])
        self.assertTrue(self.engine.is_stalemate)
