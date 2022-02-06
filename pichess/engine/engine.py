from pichess.utils import fen_to_matrix


class Engine:
    def __init__(self):
        pass

    def set_fen_position(self, fen) -> None:
        '''set position from fen string'''

        self.matrix = fen_to_matrix(fen)
