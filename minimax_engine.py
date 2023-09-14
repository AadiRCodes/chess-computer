import chess
import chess.polyglot
from evaluation import evaluate
n = 0
minimax_table = {}
pos_hash = chess.polyglot.zobrist_hash
def max_value(board, depth, alpha, beta):
    score = float("-inf")
    best_move = None
    ordered_moves = move_ordering(board, board.legal_moves)
    for move in ordered_moves:
        board.push(move)
        if board.is_checkmate():
            board.pop()
            return (move, float("inf"))
        nextScore = 0
        h = pos_hash(board)
        if h in minimax_table.keys():
            nextScore = minimax_table[h]
        else:
            nextScore = minimax(board, depth-1, False, alpha, beta)[1]
            minimax_table[h] = nextScore
        if nextScore > score:
            score = nextScore
            best_move = move
        board.pop()
        if score >= beta:
            return (best_move, score)
        alpha = max(alpha, score)
    return (best_move, score)
    
def min_value(board, depth, alpha, beta):
    score = float("inf")
    best_move = None
    ordered_moves = move_ordering(board, board.legal_moves)
    for move in ordered_moves:
        board.push(move)
        if board.is_checkmate():
            board.pop()
            return (move, float("-inf"))
        h = pos_hash(board)
        if h in minimax_table.keys():
            nextScore = minimax_table[h]
        else:
            nextScore = minimax(board, depth-1, True, alpha, beta)[1]
            minimax_table[h] = nextScore
        if nextScore < score:
            score = nextScore
            best_move = move     
        board.pop()       
        if score <= alpha:
            return (best_move, score)
        beta = min(beta, score)
    return (best_move, score)

def minimax(board, depth, is_maximizing, alpha, beta):
    global n
    n+=1
    print("Call", n)
    if depth == 0 or board.is_game_over():
        return (None, evaluate(board))
    elif is_maximizing:
        return max_value(board, depth, alpha, beta)
    else:
        return min_value(board, depth, alpha, beta)
    
def make_move(board, depth=4):
    if board.turn == chess.WHITE:
        return minimax(board, depth, True, float("-inf"), float("inf"))[0]
    if board.turn == chess.BLACK:
        return minimax(board, depth, False, float("-inf"), float("inf"))[0]

def move_ordering(board, moves):
    def is_promotion(move):
        if move.promotion != None:
            return True
    def is_check(board, move):
        if board.gives_check(move):
            return True
    def is_capture(board, move):
        if board.piece_at(move.to_square):
            return True
    promotions = [move for move in moves if is_promotion(move)]
    checks = [move for move in moves if is_check(board, move)]
    captures = [move for move in moves if is_capture(board, move)]
    ordered_moves = [move for move in moves if (move not in promotions) or (move not in checks) or (move not in captures)]
    return ordered_moves
