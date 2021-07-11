import json
from os import path
import os
import sys
from time import sleep
from random import randint

# TODO:
# screen -> 64 width


class Character:
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

        with open("models/attacks.json") as f:
            attacks = json.load(f)
            self.attacks = attacks[self.clas]

        self.hp = character['hp']
        self.mana = character['mana']
        self.money = character['money']
        self.currentLocation = character['currentLocation']
        self.seenFightingLocation = character['seenFightingLocation']

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
        character['seenFightingLocation'] = self.seenFightingLocation

        with open("character.json", "w") as f:
            json.dump(character, f)

    def play_intro(*args):
        print("Witaj! Musisz stworzyc swoja postac!")
        print("Podaj swoje imie poszukiwaczu przygod: ")
        name = input()
        print("Wybierz klase: ")
        clas = input("1. <Wojownik> 2. <Lucznik> 3. <Mag>\n\n")
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


class Enemy:
    def __init__(self, ch, story):
        e = story[ch.currentLocation]["enemy"]
        self.hp = e["hp"]
        self.attacksDescription = e["attacksDescription"]
        self.attacksDMG = e["attacksDMG"]
        self.getDMG = e["getDMG"]
        self.defeated = e["deafeted"]


def clear_console():
    command = "clear"
    if os.name in ("nt", "dos"):
        command = "cls"
    os.system(command)


def deleteCharacter():
    os.remove("character.json")
    sleep(1)


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


def attack(at, ch, enemy, story):
    defense = 0
    at = which_option(at, ch.attacks)
    for i, item in enumerate(ch.eq.items()):
        if i == 0:
            weapon = item
        if i == 1:
            blocker = item
        if i == 2:
            break

    if at == 1:
        enemy.hp -= weapon[1][0]
        ch.eq[weapon[0]][1] -= 1

    if at == 2:
        enemy.hp -= 1.5 * weapon[1][0]
        ch.eq[weapon[0]][1] -= 2

    if at == 3:
        if ch.clas == "Wojownik":
            addDef = 15
        elif ch.clas == "Lucznik":
            addDef = 10
        else:
            addDef = 5

        defense = addDef + blocker[1][0]//4

        ch.eq[blocker[0]][1] -= 1

    if at == 4:
        if ch.clas == "Mag":
            addHeal = 15
        elif ch.clas == "Lucznik":
            addHeal = 10
        else:
            addHeal = 5
        ch.hp += addHeal + blocker[1][0]//8

    return defense


def fight(ch, story):
    enemy = Enemy(ch, story)
    defense = 0
    while True:
        # enemy turn
        randomNumber = randint(0, 3)
        text = "ENEMY HP: " + str(enemy.hp) + "\n\n" + \
            enemy.attacksDescription[randomNumber]
        if defense >= enemy.attacksDMG[randomNumber]:
            pass
        else:
            ch.hp -= enemy.attacksDMG[randomNumber]-defense
        options = ch.attacks
        print_screen(text, ch.hp, ch.mana, ch.money, options)
        # player turn
        at = input()
        defense = attack(at, ch, enemy, story)

        if enemy.hp <= 0:
            print(enemy.defeated)
            wait = input()
            break
        if ch.hp <= 0:
            print("UMRAŁEŚ")
            deleteCharacter()
            wait = input()
            sys.exit(1)

        text = enemy.getDMG[randomNumber]
        print(text)
        wait = input()


def makeMove(decision, options, optionsType, directions, ch):
    op = (which_option(decision, options))-1
    if optionsType[op] == "move":
        ch.currentLocation = directions[op]
    if optionsType[op] == "eq":
        print_eq(ch)


def play(story, ch):
    # variables
    currentLocation = ch.currentLocation
    text = story[currentLocation]['text']
    directions = story[currentLocation]['directions']
    options = story[currentLocation]['options']
    optionsType = story[currentLocation]['optionsType']

    if story[ch.currentLocation]["fightingLocation"] and ch.currentLocation not in ch.seenFightingLocation:
        ch.seenFightingLocation.append(ch.currentLocation)

        text1 = story[currentLocation]['text1']
        print(text1)
        while True:
            fight(ch, story)
            break

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

        makeMove(decision, options, optionsType, directions, ch)
        flag = False


def main():
    ch = Character()

    with open("story.json") as f:
        story = json.load(f)

    while True:
        play(story, ch)


if __name__ == '__main__':
    main()
