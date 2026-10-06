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


def describe_room(state):
    if state["room"] == "hallway":
        print("There is a wall sconce that contains a candle to your right, and a door to your left.")
    elif state["room"] == "chamber":
        print("You are in a small stone chamber. The floor is covered in moss.")
        print("A towering white fountain with blue tint is just ahead, and the hallway door is still open behind you.")


# load the game from the save file or start a new game
state = load_game()

if state is None:
    # Brand new game
    print("You light a candle in your hand and see an empty hallway lined with doors and windows and unlit wall sconces.")
    name = input("What is your name? ")
    state = {"name": name, "sconce_lit": False, "room": "hallway", "has_key": False}
    print("Welcome,", state["name"] + "!")
else:
    # Old save files may be missing the newer entries, so fill them in
    state.setdefault("room", "hallway")
    state.setdefault("has_key", False)
    print("Welcome back,", state["name"] + "!")

describe_room(state)
print("(Type 'save' to save your game or 'quit' to leave.)")

# game loop
while True:
    # pick the question based on which room we're in
    if state["room"] == "hallway":
        prompt = "Do you go to the 'door' or do you light the 'sconce'? "
    elif state["room"] == "chamber":
        prompt = "Do you 'look' around, try the 'gate', or go 'back' to the hallway? "

    choice = input(prompt).lower()

    # commands that work in every room
    if choice == "save":
        save_game(state)

    elif choice == "quit":
        print("Goodbye,", state["name"] + "!")
        break

    # hallway
    elif state["room"] == "hallway":
        if choice == "door":
            if state["sconce_lit"]:
                print("The door swings open with a creak. You step through into the darkness.")
                state["room"] = "chamber"
                describe_room(state)
                save_game(state)
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

        else:
            print("You stand in the hallway, feeling a gentle breeze coming from down the hall.")

    # chamber
    elif state["room"] == "chamber":
        if choice == "look":
            if state["has_key"]:
                print("You find nothing else of interest.")
            else:
                state["has_key"] = True
                print("Beneath the moss, your fingers find a rusty key!")

        elif choice == "gate":
            if state["has_key"]:
                print("The key breaks in the lock and the gate creaks open.")
                break
            else:
                print("The gate is locked.")

        elif choice == "back":
            state["room"] = "hallway"
            describe_room(state)

        else:
            print("Water sprinkles onto the stone floor from the splashback of the fountain.")
