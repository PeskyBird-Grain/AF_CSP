# Team members: [Add initials here]
# Class Period: [Add period here]
# Assignment: Text Adventure Game
# Game: The Lost Temple

import json
import os

# -----------------------------------------------
# SECTION 1: Game data and saved results
# Written by: [Team member initials]
# This section stores room information, items,
# and the best results from previous playthroughs.
# -----------------------------------------------

SAVE_FILE = "game_results.json"

rooms = {
    "entrance": {
        "description": "You stand at the entrance of a mysterious lost temple.",
        "exits": {"north": "hallway"},
        "items": ["torch"]
    },
    "hallway": {
        "description": "A dark hallway stretches through the ancient temple.",
        "exits": {
            "south": "entrance",
            "east": "library",
            "north": "treasure_room"
        },
        "items": ["key"]
    },
    "library": {
        "description": "An old library filled with dusty books and strange symbols.",
        "exits": {"west": "hallway"},
        "items": ["map", "gem"]
    },
    "treasure_room": {
        "description": "A treasure room with a locked golden chest!",
        "exits": {"south": "hallway"},
        "items": ["coin"]
    }
}

# Read saved results, or use defaults if no save file exists.
def load_results():
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Save file could not be read. Starting fresh.")

    return {
        "games_played": 0,
        "best_items": 0,
        "wins": 0
    }


# Save results so they carry over to the next playthrough.
def save_results(results):
    try:
        with open(SAVE_FILE, "w") as file:
            json.dump(results, file, indent=4)
    except OSError:
        print("Warning: Your results could not be saved.")


# -----------------------------------------------
# SECTION 2: Room descriptions and player movement
# Written by: [Team member initials]
# These functions display rooms and let the player
# travel through the temple.
# -----------------------------------------------

def look(room_name):
    room = rooms[room_name]

    print("\n" + room["description"])

    if room["items"]:
        print("You see:", ", ".join(room["items"]))
    else:
        print("There are no items left in this room.")

    print("Exits:", ", ".join(room["exits"].keys()))


def move(direction, current_room):
    room = rooms[current_room]

    if direction in room["exits"]:
        new_room = room["exits"][direction]
        print("You travel", direction + ".")
        return new_room
    else:
        print("You cannot go that way.")
        return current_room


# -----------------------------------------------
# SECTION 3: Inventory and item collection
# Written by: [Team member initials]
# This section lets the player collect and inspect
# items found in different rooms.
# -----------------------------------------------

def take_item(item, current_room, inventory):
    room_items = rooms[current_room]["items"]

    if item in room_items:
        inventory.append(item)
        room_items.remove(item)
        print("You collected the", item + "!")
    else:
        print("That item is not here.")


def show_inventory(inventory):
    if inventory:
        print("Your inventory:", ", ".join(inventory))
    else:
        print("Your inventory is empty.")


# -----------------------------------------------
# SECTION 4: Puzzle and game ending
# Written by: [Team member initials]
# The player needs the key to open the chest.
# The player wins by opening the chest and escapes
# safely, or loses by running out of moves.
# -----------------------------------------------

def use_item(item, current_room, inventory):
    if item not in inventory:
        print("You do not have that item.")
        return "playing"

    if item == "torch":
        print("You light the torch. The dark temple is easier to explore.")

    elif item == "map":
        print("The map shows the temple layout:")
        print("Entrance -> Hallway -> Treasure Room")
        print("                 |")
        print("              Library")

    elif item == "gem":
        print("The gem glows mysteriously in your hand.")

    elif item == "coin":
        print("The ancient coin bears the image of a forgotten king.")

    elif item == "key":
        if current_room == "treasure_room":
            print("You use the key to unlock the golden chest!")
            print("Inside, you discover the legendary treasure!")
            return "won"
        else:
            print("The key might unlock something deeper in the temple.")

    else:
        print("You cannot use that item right now.")

    return "playing"


# -----------------------------------------------
# SECTION 5: Main game loop
# Written by: [Team member initials]
# This section displays instructions, accepts
# commands, tracks moves, and ends the game.
# -----------------------------------------------

def play_game():
    results = load_results()

    print("=" * 40)
    print("       THE LOST TEMPLE")
    print("=" * 40)
    print("Find the key and unlock the treasure chest!")
    print("\nCommands:")
    print("  go north / go south / go east / go west")
    print("  look")
    print("  take [item]")
    print("  use [item]")
    print("  inventory")
    print("  help")
    print("  quit")
    print("\nYou have 20 moves to find the treasure.")
    print("Be careful: leaving without the treasure is no victory!")

    current_room = "entrance"
    inventory = []
    moves = 0
    game_status = "playing"

    # Show the starting room.
    look(current_room)

    while game_status == "playing":
        command = input("\nWhat do you want to do? ").strip().lower()

        if not command:
            print("Please enter a command.")
            continue

        # Quit allows the player to leave the adventure.
        if command == "quit":
            print("You leave the temple without the treasure.")
            game_status = "lost"

        elif command == "help":
            print("Explore rooms, collect items, and use the key")
            print("in the treasure room to win.")

        elif command == "look":
            look(current_room)

        elif command == "inventory":
            show_inventory(inventory)

        elif command.startswith("go "):
            direction = command[3:].strip()

            if direction in ["north", "south", "east", "west"]:
                current_room = move(direction, current_room)
                moves += 1
                look(current_room)
            else:
                print("Invalid direction. Try north, south, east, or west.")

        elif command.startswith("take "):
            item = command[5:].strip()

            if item:
                before = len(inventory)
                take_item(item, current_room, inventory)

                if len(inventory) > before:
                    moves += 1
            else:
                print("Specify an item, such as 'take torch'.")

        elif command.startswith("use "):
            item = command[4:].strip()

            if item:
                game_status = use_item(item, current_room, inventory)

                if game_status == "playing":
                    moves += 1
            else:
                print("Specify an item, such as 'use key'.")

        else:
            print("Unknown command. Type 'help' to see available commands.")

        # Lose if the player uses all 20 moves.
        if game_status == "playing" and moves >= 20:
            print("\nYou ran out of moves!")
            print("The temple doors seal shut. Game over!")
            game_status = "lost"

    # -------------------------------------------
    # SECTION 6: Update and display saved results
    # Written by: [Team member initials]
    # This section updates the file after each game.
    # -------------------------------------------

    results["games_played"] += 1
    items_collected = len(inventory)

    if game_status == "won":
        results["wins"] += 1
        print("\nCongratulations! You escaped with the treasure!")
        print("Moves used:", moves)
    else:
        print("\nGame over. Better luck next time!")

    if items_collected > results["best_items"]:
        results["best_items"] = items_collected

    save_results(results)

    print("\n" + "=" * 40)
    print("         PLAYTHROUGH RESULTS")
    print("=" * 40)
    print("Items collected this run:", items_collected)
    print("Moves used this run:", moves)
    print("Games played total:", results["games_played"])
    print("Total wins:", results["wins"])
    print("Best items collected in one run:", results["best_items"])
    print("=" * 40)


# Start the game.
if __name__ == "__main__":
    play_game()