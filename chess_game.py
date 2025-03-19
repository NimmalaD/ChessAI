import chess
from colorama import Fore, Style
from ai_agent import get_best_move

# Create chess board
board = chess.Board()

print(Fore.GREEN + "Initial Chess Board:")
print(board)
print(Style.RESET_ALL)

while not board.is_game_over():
    print(Fore.YELLOW + "\nLegal Moves:")
    print([move.uci() for move in board.legal_moves])
    print(Style.RESET_ALL)

    # Human move
    move_input = input("Enter your move (e.g., e2e4): ").strip()

    try:
        move = chess.Move.from_uci(move_input)
        if move in board.legal_moves:
            board.push(move)
            print(Fore.GREEN + "\nBoard after your move:")
            print(board)
            print(Style.RESET_ALL)
        else:
            print(Fore.RED + "Illegal move! Try again." + Style.RESET_ALL)
            continue
    except:
        print(Fore.RED + "Invalid move format! Try again." + Style.RESET_ALL)
        continue

    # Check if game is over
    if board.is_game_over():
        break

    # AI Move
    print(Fore.BLUE + "\nAI is thinking...")
    ai_move = get_best_move(board, 5)  # Depth = 3 (you can increase later)
    if ai_move:
        board.push(ai_move)
        print(Fore.BLUE + f"AI plays: {ai_move.uci()}")
        print(board)
    else:
        print(Fore.RED + "No valid move for AI." + Style.RESET_ALL)
