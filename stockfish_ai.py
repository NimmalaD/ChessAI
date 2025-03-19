from stockfish import Stockfish

# Set the path to your Stockfish executable
stockfish = Stockfish(path="/Users/dharma/Downloads/stockfish/stockfish-macos-m1-apple-silicon")  # Replace with actual path

# Set the skill level (optional: from 0 to 20)
stockfish.set_skill_level(15)

def get_stockfish_best_move(fen):
    stockfish.set_fen_position(fen)
    best_move = stockfish.get_best_move()
    return best_move
