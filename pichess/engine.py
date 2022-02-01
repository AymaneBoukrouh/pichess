from __future__ import annotations
from pichess.utils import fen_to_matrix
from abc import ABC, abstractmethod


class Engine:
    pass


class Piece(ABC):
    def __init__(self, coordinates: str=None, color: bool=True):
        self.coordinates = coordinates
        self.color = color # True -> white, False -> black

    @property
    @abstractmethod
    def all_move_directions(self) -> set[tuple[int, int]]:
        '''
        return a set of (x, y) pair used to determine the moves
        that the piece can make from a relative position (0, 0)

        x represents the horizontal steps (files)
        y represents the vertical steps (ranks)
        '''

    @property
    def possible_move_coordinates(self) -> set[str]:
        '''return a set of possible move coordinates a piece can go to'''
        
        directions = self.all_move_directions
        return self.coordinates_from_directions(self.coordinates, directions)

    @property
    @abstractmethod
    def all_capture_directions(self) -> set[tuple[int, int]]:
        '''
        return a set of (x, y) pair used to determine the captures
        that the piece can make from a relative position (0, 0)
        
        x represents the horizontal steps (files)
        y represents the vertical steps (ranks) 
        '''

    @property
    def possible_capture_coordinates(self) -> set[str]:
        '''return a set of possible capture coordinates a piece can make'''

        directions = self.all_capture_directions
        return self.coordinates_from_directions(self.coordinates, directions)

    @staticmethod
    def coordinates_from_directions(coordinates:str, directions: set[tuple[int, int]]):
        '''return set of coordinates from a set of directions from current coordinates'''

        current_file: str = coordinates[0]
        current_rank: int = int(coordinates[1])

        coordinates_set = set()
        for (x, y) in directions:
            file: str = chr(ord(current_file) + x)
            rank: int = current_rank + y

            if (1 <= rank <= 8) and (ord('a') <= ord(file) <= ord('h')):
                coordinates_set.add(f'{file}{rank}')
        
        return coordinates_set


class King(Piece):
    @property
    def all_move_directions(self):
        return {
            (-1,  1), (0,  1), (1,  1),
            (-1,  0),          (1,  0),
            (-1, -1), (0, -1), (1, -1)
        }

    @property
    def all_capture_directions(self):
        return self.all_move_directions


class Queen(Piece):
    @property
    def all_move_directions(self):
        bishop = Bishop(self.coordinates)
        rook = Rook(self.coordinates)

        return {
            *rook.all_move_directions,
            *bishop.all_move_directions
        }

    @property
    def all_capture_directions(self):
        return self.all_move_directions


class Rook(Piece):
    @property
    def all_move_directions(self):
        return {
            *[(x, 0) for x in range(-8, 0)],
            *[(x+1, 0) for x in range(8)],
            *[(0, y) for y in range(-8, 0)],
            *[(0, y+1) for y in range(8)]
        }
    
    @property 
    def all_capture_directions(self):
        return self.all_move_directions


class Bishop(Piece):
    @property
    def all_move_directions(self):
        return {
            *[(x, x) for x in range(-8, 0)],
            *[(x+1, x+1) for x in range(8)],
            *[(x, -x) for x in range(-8, 0)],
            *[(x+1, -(x+1)) for x in range(8)]
        }
    
    @property
    def all_capture_directions(self):
        return self.all_move_directions


class Knight(Piece):
    @property
    def all_move_directions(self):
        return {
            (-2, 1), (-1, 2), (1, 2), (2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        }
    
    @property
    def all_capture_directions(self):
        return self.all_move_directions


class Pawn(Piece):
    @property
    def all_move_directions(self):
        rank: int = int(self.coordinates[1])

        if self.color:
            if rank == 2:
                return {(0, 1), (0, 2)}
            elif rank == 8:
                return set()
            else:
                return {(0, 1)}

        else:
            if rank == 7:
                return {(0, -1), (0, -2)}
            elif rank == 1:
                return set()
            else:
                return {(0, -1)}
    
    @property
    def all_capture_directions(self):
        rank: int = int(self.coordinates[1])

        if self.color:
            if rank != 8:
                return {(-1, 1), (1, 1)}
            else:
                return set()
        
        else:
            if rank != 1:
                return {(-1, -1), (1, -1)}
            else:
                return set()
