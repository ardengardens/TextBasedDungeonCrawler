#!/usr/bin/python3
import json
import os

SAVE_FILE = "savegame.json"


def save_game(state):
    with open(SAVE_FILE, "w") as f:
        json.dump(state, f)
    print("Game saved!")


def load_game():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE) as f:
            return json.load(f)
    return None


# --- Start of the game ---
state = load_game()

if state is None:
    # Brand new game
    print("You light a candle in your hand and see an empty hallway lined with doors and windows and unlit wall sconces.")
    name = input("What is your name? ")
    state = {"name": name, "sconce_lit": False}
    print("Welcome,", state["name"] + "!")
else:
    # Returning player
    print("Welcome back,", state["name"] + "!")
    if state["sconce_lit"]:
        print("The sconce is still lit, and the hallway glows softly.")

print("There is a wall sconce that contains an unlit candle to your right, and a closed door to your left.")
print("(Type 'save' to save your game or 'quit' to leave.)")

# --- Game loop ---
while True:
    choice = input("Do you go to the 'door' or do you light the 'sconce'? ").lower()

    if choice == "door":
        if state["sconce_lit"]:
            print("The door swings open with a creak. You step through into the darkness beyond.")
            print("WIP To be continued")
            break
        else:
            print("You turn the door knob, but the door won't budge.")
            print("Maybe there's a way to get the door to open.")

    elif choice == "sconce":
        if state["sconce_lit"]:
            print("The sconce is already lit.")
        else:
            state["sconce_lit"] = True
            print("You lift your candle to light the wall sconce.")
            print("The candle is lit, and you hear a clicking sound coming from the door behind you.")

    elif choice == "save":
        save_game(state)

    elif choice == "quit":
        print("Goodbye,", state["name"] + "!")
        break

    else:
        print("You stand in the hallway, feeling a gentle breeze coming from down the hall.")
