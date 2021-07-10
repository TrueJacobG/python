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

            name, clas, eq = self.play_intro()
            self.name = name
            self.clas = clas
            self.eq = eq

        else:
            with open("character.json") as f:
                character = json.load(f)

            self.name = character['name']
            self.clas = character['clas']
            self.eq = character['eq']

        self.hp = character['hp']
        self.mana = character['mana']
        self.money = character['money']
        self.currentLocation = character['currentLocation']

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
        print("Witaj! Musisz stworzyc swoja postac!")
        print("Podaj swoje imie poszukiwaczu przygod: ")
        name = input()
        print("Wybierz klase: ")
        clas = input("1. <Wojownik> 2. <Lucznik> 3. <Mag>")
        if clas == str(1) or clas.lower() == "wojownik":
            clas = "Wojownik"
            eq = {"Zwykly miecz": [80, 10],
                  "Zwykla tarcza": [80, 10]}
        elif clas == str(2) or clas.lower() == "lucznik":
            clas = "Lucznik"
            eq = {"Zwykly luk": [80, 10],
                  "Dziwny naszyjnik": [80, 10]}
        else:
            clas = "Mag"
            eq = {"Stara rozdzka": [80, 10],
                  "Slomiany kapelusz": [80, 10]}

        print("\n Swietnie! Decyzje dokonujesz poprzez wpisanie odpowiedniego wyboru lub numeru. Jesli chcesz zamknac gre wpisz QUIT. Pomoc -> help")

        wait = input()

        return name, clas, eq


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


def print_help():
    print("Komendy: ")
    print("help -> Wyswietlenie pomocy")
    print("quit -> Zapisanie i zamkniecie gry")
    print("\n")
    print("W kazdej lokalizacji mozesz dokonac 4 decyzji. Dokonujesz wyboru poprzez wpisanie odpowiedzi lub podanie numeru (1,2,3,4). Zatwierdzasz wybor klawiszem ENTER.")
    wait = input()


def print_screen(text, hp, mana, money, options):
    clear_console()
    print("\033[92m", text, "\033[0m")
    print("\n")
    print(
        f'           \033[91mHP: {hp}/100\033[0m     \033[94mMANA: {mana}/100\033[0m    \033[93mMONEY: {money}\033[0m')
    print_options(*options)


def print_eq(ch):
    eq = ch.eq
    print("W twoim plecaku znajduja sie: ")
    for item in eq.items():
        print(f"{item[0]} Obr: {item[1][0]} Wyt: {item[1][1]}")
    wait = input()


def which_option(decision, options):
    if decision.lower().replace(" ", "") == options[0].lower().replace(" ", "") or decision == str(1):
        return 1
    if decision.lower().replace(" ", "") == options[1].lower().replace(" ", "") or decision == str(2):
        return 2
    if decision.lower().replace(" ", "") == options[2].lower().replace(" ", "") or decision == str(3):
        return 3
    if decision.lower().replace(" ", "") == options[3].lower().replace(" ", "") or decision == str(4):
        return 4
    return None


def make_move(decision, options, options_type, directions, ch):
    op = (which_option(decision, options))-1
    if options_type[op] == "move":
        ch.currentLocation = directions[op]
    if options_type[op] == "eq":
        print_eq(ch)


def play(story, ch):
    # variables
    currentLocation = ch.currentLocation
    text = story[currentLocation]['text']
    directions = story[currentLocation]['directions']
    options = story[currentLocation]['options']
    options_type = story[currentLocation]['options_type']

    print_screen(text, ch.hp, ch.mana, ch.money, options)

    decision = input()
    flag = True
    while flag:
        if decision.lower() == "quit":
            ch.save_character()
            clear_console()
            print("Do zobaczenia niedługo :D")
            sleep(1)
            clear_console()
            flag = False
            sys.exit()
        if decision.lower() == "help":
            print_help()
            print("Co chcesz zrobić?")
            decision = input()
            continue

        if which_option(decision, options) == None:
            print("Nie rozumiem cie...")
            decision = input()
            continue

        make_move(decision, options, options_type, directions, ch)
        flag = False


def main():
    ch = Character()

    with open("story.json") as f:
        story = json.load(f)

    while True:
        play(story, ch)


if __name__ == '__main__':
    main()
