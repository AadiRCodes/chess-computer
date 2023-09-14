import chess
import piece_tables

PIECEVALUES = {
    chess.PAWN : 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 30000
}
pawn_dicts = (piece_tables.convert_to_dict(chess.PAWN, chess.WHITE),piece_tables.convert_to_dict(chess.PAWN, chess.BLACK))
knight_dicts = (piece_tables.convert_to_dict(chess.KNIGHT, chess.WHITE),piece_tables.convert_to_dict(chess.KNIGHT, chess.BLACK))
bishop_dicts = (piece_tables.convert_to_dict(chess.BISHOP, chess.WHITE),piece_tables.convert_to_dict(chess.BISHOP, chess.BLACK))
rook_dicts = (piece_tables.convert_to_dict(chess.ROOK, chess.WHITE),piece_tables.convert_to_dict(chess.ROOK, chess.BLACK))
queen_dicts = (piece_tables.convert_to_dict(chess.QUEEN, chess.WHITE),piece_tables.convert_to_dict(chess.QUEEN, chess.BLACK))
king_dicts = (piece_tables.convert_to_dict(chess.KING, chess.WHITE),piece_tables.convert_to_dict(chess.KING, chess.BLACK))

def material_score(board: chess.Board) -> int:
    """Returns the total numerical score of the material of White and Black, and returns as a tuple.
    
    Examples:
    In the starting position: Everyone has all pieces, so we have
    (34000, 34000).

    In a Queen v. Pawn ending (White has a queen and king and Black has a king and pawn), we should have
    (30900, 30100).
    """
    white_material = 0
    black_material = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece != None:
            if piece.color == chess.WHITE:
                white_material += PIECEVALUES[piece.piece_type]
            else:
                black_material += PIECEVALUES[piece.piece_type]
    return (white_material, black_material) 

def evaluate(board: chess.Board) -> float:
    material = material_score(board)
    return 1000*(material[0]-material[1])



