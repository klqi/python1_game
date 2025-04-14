## initial game and player set up
from .rooms import get_rooms
from .player import create_player

# set up game state (rooms, player, current room, game status)
def initialize_game():
    rooms = get_rooms()
    player = create_player()
    game_state = {
        "rooms": rooms,
        "player": player,
        "current_room": "start",
        "game_active": True
    }
    return game_state
