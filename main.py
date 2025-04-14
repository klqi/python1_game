# script that starts and initializes the game
from game.setup import initialize_game
from game.game_loop import play_game
from game.file_io import load_game

# choose to either start new game or load saved game
def main():
    print("Welcome to the Text Adventure Game!")
    print("1. Start a New Game")
    print("2. Load Saved Game")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "2":
        game_state = load_game()
        if game_state:
            print("Game loaded successfully!\n")
        else:
            print("No saved game found or error loading. Starting a new game.\n")
            game_state = initialize_game()
    else:
        game_state = initialize_game()

    play_game(game_state)

if __name__ == "__main__":
    main()
