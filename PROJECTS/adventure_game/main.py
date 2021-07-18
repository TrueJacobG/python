import json
from os import path
import os
import sys
from time import sleep
from random import randint
from random import uniform
# TODO:
# screen -> 64 width


class Game:
    def __init__(self, story):
        self.story = story

    @staticmethod
    def clear_console():
        command = "clear"
        if os.name in ("nt", "dos"):
            command = "cls"
        os.system(command)

    @staticmethod
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

    def print_help(self):
        print("Komendy: ")
        print("help -> Wyswietlenie pomocy")
        print("quit -> Zapisanie i zamkniecie gry")
        print("\n")
        print("W kazdej lokalizacji mozesz dokonac 4 decyzji. Dokonujesz wyboru poprzez wpisanie odpowiedzi lub podanie numeru (1,2,3,4). Zatwierdzasz wybor klawiszem ENTER.")
        wait = input()

    @staticmethod
    def print_screen(text, hp, mana, money, options):
        Game.clear_console()
        print("\033[92m", text, "\033[0m")
        print("\n")
        print(
            f'           \033[91mHP: {hp}/100\033[0m     \033[94mMANA: {mana}/100\033[0m    \033[93mMONEY: {money}\033[0m')
        Game.print_options(*options)

    @staticmethod
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

    @staticmethod
    def drop_money(enemy_hp):
        return int(enemy_hp * 0.1 * uniform(1.0, 2.0))


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

    def play_intro(self, *args):
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

    def deleteCharacter(self):
        os.remove("character.json")
        sleep(1)

    def print_eq(self):
        eq = self.eq
        print("W twoim plecaku znajduja sie: ")
        for item in eq.items():
            print(f"{item[0]} Att/Obr: {item[1][0]} Wyt: {item[1][1]}")
        wait = input()

    def attack(self, at, enemy, story):
        defense = 0
        at = Game.which_option(at, self.attacks)
        for i, item in enumerate(self.eq.items()):
            if i == 0:
                weapon = item
            if i == 1:
                blocker = item
            if i == 2:
                break

        if at == 1:
            enemy.hp -= weapon[1][0]
            self.eq[weapon[0]][1] -= 1

        if at == 2:
            enemy.hp -= 1.5 * weapon[1][0]
            self.eq[weapon[0]][1] -= 2

        if at == 3:
            if self.clas == "Wojownik":
                addDef = 15
            elif self.clas == "Lucznik":
                addDef = 10
            else:
                addDef = 5

            defense = addDef + blocker[1][0]//4

            self.eq[blocker[0]][1] -= 1

        if at == 4:
            if self.clas == "Mag":
                addHeal = 15
            elif self.clas == "Lucznik":
                addHeal = 10
            else:
                addHeal = 5
            self.hp += addHeal + blocker[1][0]//8

        return defense

    def shop(self, op, GAME):
        whichShelf = GAME.story[self.currentLocation]["directions"][op]
        shelf = GAME.story[self.currentLocation]["shop"][whichShelf][self.clas]
        for item in shelf.items():
            print(item[0], " --- ", "\033[91mAtt/Obr: ", item[1][0],
                  "\033[0m\033[95mWyt: ", item[1][1], "\033[0m\033[93mCena: ", item[1][2], "\033[0m")

        print("Na co masz ochote?")
        decision = input()
        try:
            decision = (Game.which_option(decision, list(shelf.keys())))-1
        except:
            return

        boughtItemName = list(shelf)[decision]
        boughtItemStats = shelf[boughtItemName]
        if self.money < boughtItemStats[2]:
            print("Nie masz wystarczajaco pieniedzy! Wynocha z mojego sklepu!")
            wait = input()
            return
        if boughtItemName in self.eq:
            print("Juz posiadasz taki przedmiot!")
            wait = input()
            return
        self.money -= boughtItemStats[2]
        self.eq[boughtItemName] = boughtItemStats[0:2]
        print("Dziekuje za dokonanie u mnie zakupu :D")
        wait = input()

    def makeMove(self, decision, options, optionsType, directions, GAME):
        op = (Game.which_option(decision, options))-1
        if optionsType[op] == "move":
            self.currentLocation = directions[op]
        if optionsType[op] == "eq":
            self.print_eq()
        if optionsType[op] == "shop":
            self.shop(op, GAME)

    def fight(self, PLAYER, GAME):
        enemy = Enemy(PLAYER, GAME.story)
        hp_for_money = enemy.hp
        defense = 0
        while True:
            # enemy turn
            randomNumber = randint(0, 3)
            text = "ENEMY HP: " + str(enemy.hp) + "\n\n" + \
                enemy.attacksDescription[randomNumber]
            if defense >= enemy.attacksDMG[randomNumber]:
                pass
            else:
                self.hp -= enemy.attacksDMG[randomNumber]-defense
            options = self.attacks
            Game.print_screen(text, self.hp, self.mana, self.money, options)
            # player turn
            at = input()
            defense = self.attack(at, enemy, GAME.story)

            if enemy.hp <= 0:
                print(enemy.defeated)
                coins = Game.drop_money(hp_for_money)
                PLAYER.money += coins
                print("Za udana walke otrzymujesz ", coins, " pieniedzy!")
                wait = input()
                break
            if self.hp <= 0:
                print("UMRALES")
                self.deleteCharacter()
                wait = input()
                sys.exit(1)

            text = enemy.getDMG[randomNumber]
            print(text)
            wait = input()


class Enemy:
    def __init__(self, PLAYER, story):
        e = story[PLAYER.currentLocation]["enemy"]
        self.hp = e["hp"]
        self.attacksDescription = e["attacksDescription"]
        self.attacksDMG = e["attacksDMG"]
        self.getDMG = e["getDMG"]
        self.defeated = e["deafeted"]


def play(PLAYER, GAME):
    # variables
    currentLocation = PLAYER.currentLocation
    text = GAME.story[currentLocation]['text']
    directions = GAME.story[currentLocation]['directions']
    options = GAME.story[currentLocation]['options']
    optionsType = GAME.story[currentLocation]['optionsType']

    if GAME.story[PLAYER.currentLocation]["fightingLocation"] and PLAYER.currentLocation not in PLAYER.seenFightingLocation:
        PLAYER.seenFightingLocation.append(PLAYER.currentLocation)

        text1 = GAME.story[currentLocation]['text1']
        print(text1)
        while True:
            PLAYER.fight(PLAYER, GAME)
            break

    Game.print_screen(text, PLAYER.hp, PLAYER.mana, PLAYER.money, options)

    decision = input()
    flag = True
    while flag:
        if decision.lower() == "quit":
            PLAYER.save_character()
            Game.clear_console()
            print("Do zobaczenia niedługo :D")
            sleep(1)
            Game.clear_console()
            flag = False
            sys.exit()
        if decision.lower() == "help":
            GAME.print_help()
            print("Co chcesz zrobić?")
            decision = input()
            continue

        if Game.which_option(decision, options) == None:
            print("Nie rozumiem cie...")
            decision = input()
            continue

        PLAYER.makeMove(decision, options, optionsType, directions, GAME)
        flag = False


def main():
    with open("story.json") as f:
        story = json.load(f)

    PLAYER = Character()
    GAME = Game(story)

    while True:
        play(PLAYER, GAME)


if __name__ == '__main__':
    main()
