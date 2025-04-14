# create player and manage inventory
def create_player():
    name = input("Enter your name: ")
    return {
        "name": name,
        "inventory": [],
        "health": 100
    }
