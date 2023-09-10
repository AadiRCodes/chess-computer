import chess

PAWN_TABLE =  [[0,  0,  0,  0,  0,  0,  0,  0],
[50, 50, 50, 50, 50, 50, 50, 50],
[10, 10, 20, 30, 30, 20, 10, 10],
 [5,  5, 10, 25, 25, 10,  5,  5],
 [0,  0,  0, 20, 20,  0,  0,  0],
 [5, -5,-10,  0,  0,-10, -5,  5],
[5, 10, 10,-20,-20, 10, 10,  5],
 [0,  0,  0,  0,  0,  0,  0,  0]]

KNIGHT_TABLE = [[-50,-40,-30,-30,-30,-30,-40,-50],
[-40,-20,  0,  0,  0,  0,-20,-40],
[-30,  0, 10, 15, 15, 10,  0,-30],
[-30,  5, 15, 20, 20, 15,  5,-30],
[-30,  0, 15, 20, 20, 15,  0,-30],
[-30,  5, 10, 15, 15, 10,  5,-30],
[-40,-20,  0,  5,  5,  0,-20,-40],
[-50,-40,-30,-30,-30,-30,-40,-50]]

BISHOP_TABLE = [[-20,-10,-10,-10,-10,-10,-10,-20],
[-10,  0,  0,  0,  0,  0,  0,-10],
[-10,  0,  5, 10, 10,  5,  0,-10],
[-10,  5,  5, 10, 10,  5,  5,-10],
[-10,  0, 10, 10, 10, 10,  0,-10],
[-10, 10, 10, 10, 10, 10, 10,-10],
[-10,  5,  0,  0,  0,  0,  5,-10],
[-20,-10,-10,-10,-10,-10,-10,-20]]

ROOK_TABLE = [[0,  0,  0,  0,  0,  0,  0,  0],
  [5, 10, 10, 10, 10, 10, 10,  5],
 [-5,  0,  0,  0,  0,  0,  0, -5],
 [-5,  0,  0,  0,  0,  0,  0, -5],
 [-5,  0,  0,  0,  0,  0,  0, -5],
 [-5,  0,  0,  0,  0,  0,  0, -5],
 [-5,  0,  0,  0,  0,  0,  0, -5],
  [0,  0,  0,  5,  5,  0,  0,  0]]

QUEEN_TABLE = [[0,  0,  0,  0,  0,  0,  0,  0],
  [5, 10, 10, 10, 10, 10, 10,  5],
 [-5,  0,  0,  0,  0,  0,  0, -5],
 [-5,  0,  0,  0,  0,  0,  0, -5],
 [-5,  0,  0,  0,  0,  0,  0, -5],
 [-5,  0,  0,  0,  0,  0,  0, -5],
 [-5,  0,  0,  0,  0,  0,  0, -5],
 [0,  0,  0,  5,  5,  0,  0,  0]]

KING_TABLES = ([[-30,-40,-40,-50,-50,-40,-40,-30], # MIDDLEGAME TABLES
[-30,-40,-40,-50,-50,-40,-40,-30],
[-30,-40,-40,-50,-50,-40,-40,-30],
[-30,-40,-40,-50,-50,-40,-40,-30],
[-20,-30,-30,-40,-40,-30,-30,-20],
[-10,-20,-20,-20,-20,-20,-20,-10],
[20, 20,  0,  0,  0,  0, 20, 20],
[20, 30, 10,  0,  0, 10, 30, 20]], 
[[-50,-40,-30,-20,-20,-30,-40,-50], # ENDGAME TABLES
[-30,-20,-10,  0,  0,-10,-20,-30],
[-30,-10, 20, 30, 30, 20,-10,-30],
[-30,-10, 30, 40, 40, 30,-10,-30],
[-30,-10, 30, 40, 40, 30,-10,-30],
[-30,-10, 20, 30, 30, 20,-10,-30],
[-30,-30,  0,  0,  0,  0,-30,-30],
[-50,-30,-30,-30,-30,-30,-30,-50]])

def convert_to_dict(pieceType: chess.PieceType, color: chess.Color) -> dict:
    def conversion(array, color):
        converted_dict = {square: None for square in chess.SQUARES}
        if color == chess.WHITE:
            for square in chess.SQUARES:
                row = 7-(square//8)
                col = square%8
                converted_dict[square] = array[row][col]
        else:
            for square in chess.SQUARES:
                row = square//8
                col = 7-(square%8)
                converted_dict[square] = array[row][col]
        return converted_dict
    if pieceType == chess.PAWN:
        return conversion(PAWN_TABLE, color)
    elif pieceType == chess.KNIGHT:
        return conversion(KNIGHT_TABLE, color)
    elif pieceType == chess.BISHOP:
        return conversion(BISHOP_TABLE, color)
    elif pieceType == chess.ROOK:
        return conversion(ROOK_TABLE, color)
    elif pieceType == chess.QUEEN:
        return conversion(QUEEN_TABLE, color)
    elif pieceType == chess.KING:
        return (conversion(KING_TABLES[0], color), conversion(KING_TABLES[1], color))
