# script to save and load game status as json files
import json

# saves current game to json file
def save_game(game_state):
    try:
        with open("saved_games/savegame.json", "w") as f:
            json.dump(game_state, f)
        print("Game saved.")
    except Exception as e:
        print("Error saving game:", e)

# loads game from existing json file (unless file does not exist)
def load_game():
    try:
        with open("saved_games/savegame.json", "r") as f:
            return json.load(f)
    except Exception as e:
        print("Error loading game:", e)
        return None
