# contains main game loop and command processing
from .file_io import save_game, load_game

# displays current game status
def show_status(game_state):
    room = game_state["rooms"][game_state["current_room"]]
    print("\n" + "-"*40)
    print(f"Location: {game_state['current_room'].upper()}")
    print(room["description"])
    if room["items"]:
        print("You see:", ", ".join(room["items"]))
    print("Exits:", list(room["exits"].keys()))
    print("Inventory:", game_state["player"]["inventory"])

# processes player commands, such as moving, collecting items, saving, loading, and quitting
def process_command(command, game_state):
    current_room = game_state["current_room"]
    rooms = game_state["rooms"]
    player = game_state["player"]

    if command.startswith("go "):
        direction = command[3:]
        if direction in rooms[current_room]["exits"]:
            game_state["current_room"] = rooms[current_room]["exits"][direction]
            print(f"You move {direction}.")
        else:
            print("You can't go that way.")
    elif command.startswith("take "):
        item = command[5:]
        if item in rooms[current_room]["items"]:
            player["inventory"].append(item)
            rooms[current_room]["items"].remove(item)
            print(f"You took the {item}.")
        else:
            print("That item isn't here.")
    elif command == "save":
        save_game(game_state)
    elif command == "load":
        loaded_state = load_game()
        if loaded_state:
            game_state.update(loaded_state)
            print("Game loaded.")
    elif command == "quit":
        game_state["game_active"] = False
    elif current_room == "dungeon" and "key" in player["inventory"]:
        print("You unlock the cell and escape! YOU WIN!")
        game_state["game_active"] = False
    else:
        print("Unknown command.")

# starts and plays the game from current game status until game is inactive
def play_game(game_state):
    print(f"Welcome, {game_state['player']['name']}! Type commands like 'go north', 'take key', 'save', or 'quit'.")
    while game_state["game_active"]:
        show_status(game_state)
        command = input("\nWhat do you do? ").lower().strip()
        process_command(command, game_state)
    print("\nThanks for playing!")
