from typing import Iterator, Any
from enum import Enum


class Color(Enum):
    WHITE = 1
    BLACK = 0


def fen_to_dict(fen: str) -> dict:
    '''split fen data into a dict'''

    string, turn, castling, en_passant, halfmoves, moves = fen.split()

    return {
        'string': string,
        'turn': True if turn == 'w' else False,
        'en_passant': en_passant if en_passant != '-' else None,
        'halfmoves': int(halfmoves),
        'moves': int(moves)
    }


def fen_to_matrix(fen: str) -> dict[str, str]:
    '''convert fen to matrix'''

    matrix = {
        f'{chr(ord("a")+x)}{y+1}': None
        for x in range(8)
        for y in range(8)
    }

    x, y = 'a', 8 # start from top-left, because that's how fen works
    fen_string = fen_to_dict(fen)['string']
    for char in fen_string:
        if char.isalpha():
            matrix[f'{x}{y}'] = char
        elif char.isdigit():
            x = chr(ord(x) + int(char))
        elif char == '/':
            x, y = 'a', y-1

        if not char.isdigit() and char != '/':
            x = chr(ord(x) + 1)            

    return matrix


def generate_fen(matrix, turn, castling='-', en_passant='-', halfmoves=0, moves=0):
    '''generate fen from matrix, turn, castling, en passant, halfmoves, and moves'''

    fen_string = ''
    for y in range(8, 0, -1):
        file_count = 0
        for x in map(lambda x: chr(ord('a')+x), range(8)):
            coordinates = f'{x}{y}'
            if matrix[coordinates]:
                if file_count:
                    fen_string += str(file_count)
                    file_count = 0
                fen_string += matrix[coordinates]

            else:
                file_count += 1

        if file_count:
            fen_string += str(file_count)
        
        if y != 1:
            fen_string += '/'

    turn = 'w' if turn else 'b'
    return f'{fen_string} {turn} {castling} {en_passant} {halfmoves} {moves}'


def generator_from_args(*args: Any) -> Iterator[Any]:
    '''create a generator from *args'''

    for arg in args:
        yield arg
