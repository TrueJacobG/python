import json
from os import path
import os
import sys
from time import sleep

# TODO:
# screen -> 64 width


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


def print_options(option1, option2, option3, option4):
    option1 = " | <" + option1 + "> | "
    option2 = " | <" + option2 + "> | "
    option3 = " | <" + option3 + "> | "
    option4 = " | <" + option4 + "> | "

    filer1 = (64 - (len(option1) + len(option2)))//2
    filer2 = (64 - (len(option3) + len(option4)))//2
    filer1 = " "*filer1
    filer2 = " "*filer2

    print("################################################################")
    print(f"{filer1}{option1}{option2}{filer1}")
    print(f"{filer2}{option3}{option4}{filer2}")
    print("################################################################")


def print_screen(text, hp, mana, money, options):
    clear_console()
    print("\033[92m", text, "\033[0m")
    print("\n")
    print(
        f'           \033[91mHP: {hp}/100\033[0m     \033[94mMANA: {mana}/100\033[0m    \033[93mMONEY: {money}\033[0m')
    print_options(*options)


def getActualVariables(story, ch):
    currentLocation = ch.currentLocation

    text = story[currentLocation]['text']
    hp = ch.hp
    mana = ch.mana
    money = ch.money
    options = story[currentLocation]['options']

    return text, hp, mana, money, currentLocation, options


def play(story, ch):
    text, hp, mana, money, currentLocation, options = getActualVariables(
        story, ch)
    print_screen(text, hp, mana, money, options)
    decision = input()
    if decision.lower() == "quit":
        ch.save_character()
        clear_console()
        print("Do zobaczenia niedługo :D")
        sleep(1)
        clear_console()
        sys.exit()


def main():
    ch = Character()

    with open("story.json") as f:
        story = json.load(f)

    while True:
        play(story, ch)


if __name__ == '__main__':
    main()
