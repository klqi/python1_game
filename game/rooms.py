# set up initial rooms, can be further customized
def get_rooms():
    return {
        "start": {
            "description": "You are in a foggy clearing. Paths lead north and east.",
            "items": ["torch"],
            "exits": {"north": "library", "east": "kitchen"}
        },
        "library": {
            "description": "Dusty shelves line the walls. A staircase leads down.",
            "items": ["key"],
            "exits": {"south": "start", "down": "dungeon"}
        },
        "kitchen": {
            "description": "A rusty cauldron bubbles. You smell something foul.",
            "items": [],
            "exits": {"west": "start"}
        },
        "dungeon": {
            "description": "A dark cell with iron bars. The exit requires a key!",
            "items": [],
            "exits": {"up": "library"}
        }
    }
