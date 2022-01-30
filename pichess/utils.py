def fen_to_matrix(fen: str) -> dict[str, str]:
    """convert fen to matrix"""

    matrix = {
        f'{chr(ord("a")+x)}{y+1}': None
        for x in range(8)
        for y in range(8)
    }

    x, y = 'a', 8
    for char in fen.split()[0]:
        if char.isalpha():
            matrix[f'{x}{y}'] = char
        elif char.isdigit():
            x = chr(ord(x) + int(char))
        elif char == '/':
            x, y = 'a', y-1

        if not char.isdigit() and char != '/':
            x = chr(ord(x) + 1)            

    return matrix
