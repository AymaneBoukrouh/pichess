from __future__ import annotations
from pichess.utils import fen_to_matrix, generator_from_args
from abc import ABC, abstractmethod
from typing import Iterator


class Engine:
    def __init__(self):
        pass

    def set_fen_position(self, fen) -> None:
        '''set position from fen string'''

        self.matrix = fen_to_matrix(fen)


class Piece(ABC):
    def __init__(self, coordinates: str=None, color: bool=True):
        self.coordinates = coordinates
        self.color = color # True -> white, False -> black

    @property
    @abstractmethod
    def all_move_directions(self) -> dict[Iterator[tuple[int, int]]]:
        '''
        return a set of (x, y) pair used to determine the moves
        that the piece can make from a relative position (0, 0)

        x represents the horizontal steps (files)
        y represents the vertical steps (ranks)
        '''

    @property
    def possible_move_coordinates(self) -> set[str]:
        '''return a set of possible move coordinates a piece can go to in an empty board'''
        
        return self.directions_from_can_jump(self.all_move_directions)

    @property
    @abstractmethod
    def all_capture_directions(self) -> dict[Iterator[tuple[int, int]]]:
        '''
        return a set of (x, y) pair used to determine the captures
        that the piece can make from a relative position (0, 0)
        
        x represents the horizontal steps (files)
        y represents the vertical steps (ranks) 
        '''

    @property
    def possible_capture_coordinates(self) -> set[str]:
        '''return a set of possible capture coordinates a piece can make'''

        return self.directions_from_can_jump(self.all_capture_directions)
    
    def directions_from_can_jump(self, directions: dict[Iterator[tuple[int, int]]]):
        '''return directions depending on self.can_jump'''
        
        if not self.can_jump:
            possible_directions = self.directions_from_generators(directions)
        else:
            possible_directions = directions
        
        return self.coordinates_from_directions(self.coordinates, possible_directions)

    @staticmethod
    def coordinates_from_directions(coordinates:str, directions: set[tuple[int, int]]) -> set[str]:
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

    @staticmethod
    def directions_from_generators(direction_generators: dict[Iterator[tuple[int, int]]]) -> set[tuple[int, int]]:
        '''convert generators to a set of (x, y) directions'''

        possible_move_directions = set()
        for direction in direction_generators.keys(): # loop through cardinal directions N, NE, E, SE...
            for generated_direction in direction_generators[direction]:
                possible_move_directions.add(generated_direction)

        return possible_move_directions


class King(Piece):
    can_jump = False

    @property
    def all_move_directions(self):
        return {
            'N': generator_from_args((0, 1)),
            'NE': generator_from_args((1, 1)),
            'E': generator_from_args((1, 0)),
            'SE': generator_from_args((1, -1)),
            'S': generator_from_args((0, -1)),
            'SW': generator_from_args((-1, -1)),
            'W': generator_from_args((-1, 0)),
            'NW': generator_from_args((-1, 1))
        }

    @property
    def all_capture_directions(self):
        return self.all_move_directions


class Queen(Piece):
    can_jump = False

    @property
    def all_move_directions(self):
        bishop = Bishop(self.coordinates)
        rook = Rook(self.coordinates)

        return {
            **rook.all_move_directions,
            **bishop.all_move_directions
        }

    @property
    def all_capture_directions(self):
        return self.all_move_directions


class Rook(Piece):
    can_jump = False

    @property
    def all_move_directions(self):
        return {
            'N': ((0, y+1) for y in range(8)),
            'E': ((x+1, 0) for x in range(8)),
            'S': ((0, y-1) for y in range(0, -8, -1)),
            'W': ((x-1, 0) for x in range(0, -8, -1))
        }
    
    @property 
    def all_capture_directions(self):
        return self.all_move_directions


class Bishop(Piece):
    can_jump = False

    @property
    def all_move_directions(self):
        return {
            'NE': ((x+1, x+1) for x in range(8)),
            'SE': ((x+1, -(x+1)) for x in range(8)),
            'SW': ((x-1, x-1) for x in range(0, -8, -1)),
            'NW': ((x-1, -(x-1)) for x in range(0, -8, -1))
        }
    
    @property
    def all_capture_directions(self):
        return self.all_move_directions


class Knight(Piece):
    can_jump = True

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
    can_jump = False

    @property
    def all_move_directions(self):
        rank: int = int(self.coordinates[1])

        if self.color:
            if rank == 2:
                return {'N': generator_from_args((0, 1), (0, 2))}
            elif rank == 8:
                return dict()
            else:
                return {'N': generator_from_args((0, 1))}

        else:
            if rank == 7:
                return {'S': generator_from_args((0, -1), (0, -2))}
            elif rank == 1:
                return dict()
            else:
                return {'S': generator_from_args((0, -1))}
    
    @property
    def all_capture_directions(self):
        rank: int = int(self.coordinates[1])

        if self.color:
            if rank != 8:
                return {'N': generator_from_args((-1, 1), (1, 1))}
            else:
                return dict()
        
        else:
            if rank != 1:
                return {'S': generator_from_args((-1, -1), (1, -1))}
            else:
                return dict()
