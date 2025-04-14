from game.setup import initialize_game
from game.game_loop import play_game

def main():
    game_state = initialize_game()
    play_game(game_state)

if __name__ == "__main__":
    main()