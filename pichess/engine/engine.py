from pichess.utils import fen_to_matrix, fen_to_dict, generate_fen
from pichess.engine.pieces import Piece


class Engine:
    def __init__(self):
        pass

    def set_fen_position(self, fen: str) -> None:
        '''set position from fen string'''

        fen_dict = fen_to_dict(fen)
        self.turn = fen_dict['turn']

        self.fen = fen
        self.matrix = fen_to_matrix(fen)

        self.pieces = list()
        for coordinates in self.matrix:
            if (letter:=self.matrix[coordinates]):
                piece = Piece.from_letter(letter, coordinates)
                self.pieces.append(piece)

    @property
    def is_check(self) -> bool:
        '''return True if the king is in check, False if not'''

        king_coordinates = self.white_king_coordinates if self.turn else self.black_king_coordinates
        for piece in self.opposite_turn_pieces:
            if king_coordinates in piece.pseudolegal_coordinates(self.fen):
                return True

        return False

    @property
    def is_checkmate(self) -> bool:
        '''return True if the position is checkmate, False if not'''

        return self.is_check and not len(self.all_legal_moves)

    @property
    def is_draw(self) -> bool:
        '''return True if the position is draw, False if not'''

        matrix_pieces: list[str] = list()
        for coordinates in self.matrix:
            if self.matrix[coordinates]:
                matrix_pieces.append(self.matrix[coordinates])

        number_of_pieces = len(matrix_pieces)

        # King vs King
        if number_of_pieces == 2:
            return True

        # King and Bishop vs King
        elif number_of_pieces == 3 and any(l in matrix_pieces for l in ['b', 'B']):
            return True

        # King and Knight vs King
        elif number_of_pieces == 3 and any(l in matrix_pieces for l in ['n', 'N']):
            return True

        # King and Bishop vs King and Bishop (same color)
        
        # other
        return False

    @property
    def is_stalemate(self) -> bool:
        '''return True if the position is stalemate, False if not'''

        return not self.is_check and not len(self.all_legal_moves)

    
    def is_legal_move(self, move) -> bool:
        '''return True is move is legal, False if not'''

        start_coordinates, end_coordinates = move[:2], move[2:]
        piece = self.get_piece(start_coordinates)

        if end_coordinates not in piece.pseudolegal_coordinates(self.fen):
            return False

        tmp_matrix = self.matrix.copy()
        self.matrix[end_coordinates] = self.matrix[start_coordinates]
        self.matrix[start_coordinates] = None
        self.fen = generate_fen(self.matrix, self.turn)

        print(generate_fen(self.matrix, self.turn))

        legal_move = not self.is_check

        print(legal_move, move, self.matrix[start_coordinates], self.matrix[end_coordinates])

        self.matrix = tmp_matrix
        self.fen = generate_fen(self.matrix, self.turn)
        return legal_move

    @property
    def all_legal_moves(self) -> set[str]:
        '''return all legal moves in the position'''

        legal_moves_set = set()
        for piece in self.current_turn_pieces:
            pseudolegal_coordinates = piece.pseudolegal_coordinates(self.fen)
            for coordinates in pseudolegal_coordinates:
                move = f'{piece.coordinates}{coordinates}'
                if self.is_legal_move(move):
                    legal_moves_set.add(move)
        
        return legal_moves_set

    def get_piece(self, coordinates: str) -> Piece:
        '''return Piece at specific coordinates'''

        for piece in self.pieces:
            if piece.coordinates == coordinates:
                return piece

    @property
    def current_turn_pieces(self) -> list[Piece]:
        '''return the pieces of the player with the current turn'''

        turn = fen_to_dict(self.fen)['turn']
        return [piece for piece in self.pieces if piece.color==turn]

    @property
    def opposite_turn_pieces(self) -> list[Piece]:
        '''return the pieces of the player with the opposite turn'''

        turn = fen_to_dict(self.fen)['turn']
        return [piece for piece in self.pieces if not piece.color==turn]

    @property
    def white_king_coordinates(self) -> str:
        '''return the coordinates of the white king'''

        for coordinates in self.matrix:
            if self.matrix[coordinates] == 'K':
                return coordinates

    @property
    def black_king_coordinates(self) -> str:
        '''return the coordinates of the black king'''

        for coordinates in self.matrix:
            if self.matrix[coordinates] == 'k':
                return coordinates
