import json
from os import path
import os
import sys
from time import sleep


class Character():
    def __init__(self):
        if not path.isfile("character.json"):
            with open("models/character_model.json") as f:
                character = json.load(f)

            with open("character.json", "w") as f:
                json.dump(character, f)

            name, clas = self.play_intro()
            self.name = name
            self.clas = clas

        else:
            with open("character.json") as f:
                character = json.load(f)

            self.name = character['name']
            self.clas = character['clas']

        self.hp = character['hp']
        self.mana = character['mana']
        self.money = character['money']
        self.currentLocation = character['currentLocation']
        self.eq = character['eq']

    def save_character(self):
        with open("character.json") as f:
            character = json.load(f)

        character['name'] = self.name
        character['clas'] = self.clas
        character['hp'] = self.hp
        character['mana'] = self.mana
        character['money'] = self.money
        character['currentLocation'] = self.currentLocation
        character['eq'] = self.eq

        with open("character.json", "w") as f:
            json.dump(character, f)

    def play_intro(*args):
        print("Witaj! Musisz stworzyć swoją postać!")
        print("Podaj swoje imię poszukiwaczu przygód: ")
        name = input()
        print("Wybierz klasę: ")
        clas = input("1. <Wojownik> 2. <Łucznik> 3. <Mag>")
        if clas == 1 or clas == "Wojownik":
            clas = "Wojownik"
        elif clas == 2 or clas == "Łucznik":
            clas = "Łucznik"
        else:
            clas = "Mag"

        return name, clas


def clear_console():
    command = "clear"
    if os.name in ("nt", "dos"):
        command = "cls"
    os.system(command)


def print_options(*args):
    options = []
    for arg in args:
        options.append(arg)

    if len(options) < 4:
        empty = "-----"
        for _ in range(4-len(options)):
            options.append(empty)

    print(f"{options[0]} {options[1]}")
    print(f"{options[2]} {options[3]}")


def print_screen():
    global text, hp, mana, money, options
    clear_console()
    print(text)
    print("\n")
    print(f'HP: {hp}/100 MANA: {mana}/100 MONEY: {money}')
    print_options(options)


def play(story, cur_L):
    print(story[cur_L]["text"])
    decision = input()
    if decision.lower() == "quit":
        ch.save_character()
        clear_console()
        print("Do zobaczenia niedługo :D")
        sleep(1)
        sys.exit()


def main():

    with open("story.json") as f:
        story = json.load(f)

    with open("character.json") as f:
        character = json.load(f)

    while True:
        play(story, character["currentLocation"])


if __name__ == '__main__':
    ch = Character()
    ch.save_character()
    print(ch.name)
