import json

def load_fen(test_type: str) -> list[str]:
    '''load fen test data for engine tests'''

    with open('tests/engine/fen/fen.json') as f:
        fen = json.loads(f.read())

    return fen[test_type]
