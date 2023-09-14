import chess
from evaluation import evaluate

def max_value(board, depth, alpha, beta):
    score = float("-inf")
    best_move = None
    for move in board.legal_moves:
        board.push(move)
        nextScore = minimax(board, depth-1, False, alpha, beta)[1]
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
    for move in board.legal_moves:
        board.push(move)
        nextScore = minimax(board, depth-1, True, alpha, beta)[1]
        if nextScore < score:
            score = nextScore
            best_move = move     
        board.pop()       
        if score <= alpha:
            return (best_move, score)
        beta = min(beta, score)
    return (best_move, score)

def minimax(board, depth, is_maximizing, alpha, beta):
    
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
