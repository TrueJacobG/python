from ctypes import POINTER, WinDLL, Structure, sizeof, byref
from ctypes.wintypes import BOOL, SHORT, WCHAR, UINT, ULONG, DWORD, HANDLE
import json
from os import path
import os
import sys
from time import sleep
from random import randint
from random import uniform


# twitter.com/TrueJacobG

class Game:
    def __init__(self, story):
        self.story = story

    @staticmethod
    def terminal_size():

        LF_FACESIZE = 32
        STD_OUTPUT_HANDLE = -11

        class COORD(Structure):
            _fields_ = [
                ("X", SHORT),
                ("Y", SHORT),
            ]

        class CONSOLE_FONT_INFOEX(Structure):
            _fields_ = [
                ("cbSize", ULONG),
                ("nFont", DWORD),
                ("dwFontSize", COORD),
                ("FontFamily", UINT),
                ("FontWeight", UINT),
                ("FaceName", WCHAR * LF_FACESIZE)
            ]

        kernel32_dll = WinDLL("kernel32.dll")

        get_last_error_func = kernel32_dll.GetLastError
        get_last_error_func.argtypes = []
        get_last_error_func.restype = DWORD

        get_std_handle_func = kernel32_dll.GetStdHandle
        get_std_handle_func.argtypes = [DWORD]
        get_std_handle_func.restype = HANDLE

        get_current_console_font_ex_func = kernel32_dll.GetCurrentConsoleFontEx
        get_current_console_font_ex_func.argtypes = [
            HANDLE, BOOL, POINTER(CONSOLE_FONT_INFOEX)]
        get_current_console_font_ex_func.restype = BOOL

        set_current_console_font_ex_func = kernel32_dll.SetCurrentConsoleFontEx
        set_current_console_font_ex_func.argtypes = [
            HANDLE, BOOL, POINTER(CONSOLE_FONT_INFOEX)]
        set_current_console_font_ex_func.restype = BOOL

        stdout = get_std_handle_func(STD_OUTPUT_HANDLE)

        font = CONSOLE_FONT_INFOEX()
        font.cbSize = sizeof(CONSOLE_FONT_INFOEX)
        res = get_current_console_font_ex_func(stdout, False, byref(font))
        for field_name, _ in font._fields_:
            field_data = getattr(font, field_name)
            font.dwFontSize.X = 10
            font.dwFontSize.Y = 25
            res = set_current_console_font_ex_func(stdout, False, byref(font))

        cmd = 'mode 65, 24'
        os.system(cmd)

    @staticmethod
    def print_help():
        print("Komendy: ")
        print("help -> Wyswietlenie pomocy")
        print("eq -> Wyswietlenie eq")
        print("skills -> Wyswietlenie umiejetnosci")
        print("quit -> Zapisanie i zamkniecie gry")
        print("\n")
        print("Nie mozesz uleczyc sie ponad 100hp.")
        print("Mana odnawia Ci sie co walke.")

        print("\n")

        print("W kazdej lokalizacji mozesz dokonac 4 decyzji. Dokonujesz wyboru poprzez wpisanie odpowiedzi lub podanie numeru (1,2,3,4). Zatwierdzasz wybor klawiszem ENTER.")
        wait = input()

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

    @staticmethod
    def print_screen(text, hp, mana, money, options, currentLocation):
        Game.clear_console()
        print("Twoja lokalizacja: ", currentLocation)
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

    @staticmethod
    def getInformations(GAME, PLAYER):
        return GAME.story[PLAYER.currentLocation]['text'], GAME.story[PLAYER.currentLocation]['directions'], GAME.story[PLAYER.currentLocation]['options'], GAME.story[PLAYER.currentLocation]['optionsType'],


class Character:
    def __init__(self):
        if not path.isfile("character.json"):
            with open("models/character_model.json") as f:
                character = json.load(f)

            with open("character.json", "w") as f:
                json.dump(character, f)

            name, clas, weapon, armor = self.play_intro()
            self.name = name
            self.clas = clas
            self.isKox = False

            self.eq = {
                "weapons": weapon,
                "armors": armor
            }

        else:
            with open("character.json") as f:
                character = json.load(f)

            self.name = character['name']
            self.clas = character['clas']
            self.eq = character['eq']
            self.isKox = character['isKox']

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
        character['seenFightingLocation'] = self.seenFightingLocation
        character['eq'] = self.eq

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
            weapon = {"Zwykly miecz": [80, 10]}
            armor = {"Zwykla tarcza": [80, 10]}
        elif clas == str(2) or clas.lower() == "lucznik":
            clas = "Lucznik"
            weapon = {"Zwykly luk": [80, 10]}
            armor = {"Dziwny naszyjnik": [80, 10]}
        else:
            clas = "Mag"
            weapon = {"Stara rozdzka": [80, 10]}
            armor = {"Slomiany kapelusz": [80, 10]}

        print("\n Swietnie! Decyzje dokonujesz poprzez wpisanie odpowiedniego wyboru lub numeru. Jesli chcesz zamknac gre wpisz QUIT. Pomoc -> help")

        wait = input()

        return name, clas, weapon, armor

    def deleteCharacter(self):
        os.remove("character.json")
        sleep(1)

    def printEq(self):
        print("W twoim plecaku znajduja sie: \n")
        weapons = []
        armors = []

        for weaponType in self.eq.items():
            if weaponType[0] == "weapons":
                weapons.append(list(weaponType[1].items()))
            else:
                armors.append(list(weaponType[1].items()))

        nr = 0
        print("\033[94mBronie:\033[0m")
        for item in weapons[0]:
            nr += 1
            print(
                f"\033[93m{nr}. {item[0]}\033[0m  -  Att/Obr: {item[1][0]} Wyt: {item[1][1]}")

        nr = 0
        print("\n \033[94mZbroje:\033[0m")
        for item in armors[0]:
            nr += 1
            print(
                f"\033[93m{nr}. {item[0]}\033[0m  -  Att/Obr: {item[1][0]} Wyt: {item[1][1]}")

        print("\nChcesz zmienic swoja glowna bron i zbroje?")
        print("<TAK> <NIE>")
        decision = input()
        if decision.lower() == "tak" or decision == 1:
            self.rearrangeEq(weapons[0], armors[0])
        return

    def rearrangeEq(self, weapons, armors):

        print("Ktora bron chcesz ustawic jako glowna? (podaj numer)")
        try:
            weaponDecision = int(input())-1
        except:
            weaponDecision = 1
        print("Ktora zbroje chcesz ustawic jako glowna? (podaj numer)")
        try:
            armorDecision = int(input())-1
        except:
            armorDecision = 1

        try:
            self.eq["weapons"] = self.moveElementInDict(
                self.eq["weapons"], weapons[weaponDecision][0])

            self.eq["armors"] = self.moveElementInDict(
                self.eq["armors"], armors[armorDecision][0])
        except:
            print("Podales zly numer!")
            wait = input()

        self.printEq()

    def moveElementInDict(self, di, key):
        queue = []
        result = {}
        for item in di.items():
            if item[0] == key:
                result[item[0]] = item[1]
                continue
            queue.append(item)

        for item in queue:
            result[item[0]] = item[1]

        return result

    def attack(self, at, enemy, story):
        defense = 0
        dmg = 0
        weaponDestructionDamage = 0

        whichAttack = Game.which_option(at, self.attacks)
        weapons = []
        armors = []
        for weaponType in self.eq.items():
            if weaponType[0] == "weapons":
                weapons.append(list(weaponType[1].items()))
            else:
                armors.append(list(weaponType[1].items()))

        try:
            weapon = list(weapons[0][0])
            armor = list(armors[0][0])
        except:
            Game.clear_console()
            print("Nie masz broni lub zbroi! Twoj przeciwnik Cie nokaltuje i okrada!")
            self.money -= self.money//2
            print(
                "Zostajesz odnaleziony przez innego poszukiwacza. Przedstawil Ci sie jako Linus. Odprowadza Cie do szpitala w Eagle Town.")
            wait = input()
            return None

        weaponName = list(self.eq["weapons"].keys())[0]
        armorName = list(self.eq["armors"].keys())[0]

        if whichAttack == 1:
            dmg = 1
            weaponDestructionDamage = 1

        if whichAttack == 2:
            dmg = 1.5
            weaponDestructionDamage = 2

        enemy.hp -= weapon[1][0] * dmg
        self.eq["weapons"][weaponName][1] -= weaponDestructionDamage

        if self.eq["weapons"][weaponName][1] <= 0:
            del self.eq["weapons"][weaponName]
            print("Twoja bron ulegla zniszczeniu!")
            wait = input()

        if whichAttack == 3:
            if self.clas == "Wojownik":
                addDef = 15
            elif self.clas == "Lucznik":
                addDef = 10
            else:
                addDef = 5

            defense = addDef + armor[1][0]//4

            self.eq["armors"][armorName][1] -= 1

            if self.eq["armors"][armorName][1] <= 0:
                del self.eq["armors"][armorName]
                print("TWoja zbroja ulegla zniszczeniu!")
                wait = input()

        if whichAttack == 4:
            if self.clas == "Mag":
                addHeal = 15
            elif self.clas == "Lucznik":
                addHeal = 10
            else:
                addHeal = 5
            self.hp += addHeal + armor[1][0]//4

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
        self.eq[whichShelf][boughtItemName] = boughtItemStats[0:2]
        print("Dziekuje za dokonanie u mnie zakupu :D")
        wait = input()

    def makeMove(self, decision, options, optionsType, directions, GAME):
        op = (Game.which_option(decision, options))-1
        if optionsType[op] == "move":
            self.currentLocation = directions[op]
        if optionsType[op] == "eq":
            self.printEq()
        if optionsType[op] == "shop":
            self.shop(op, GAME)

    def fight(self, PLAYER, GAME):
        enemy = Enemy(PLAYER, GAME.story)
        hp_for_money = enemy.hp
        defense = 0
        while True:
            # enemy turn
            randomNumber = randint(0, 3)
            text = "\033[91m" + "ENEMY HP: " + str(enemy.hp) + "\n\n" + \
                enemy.attacksDescription[randomNumber] + "\033[0m"
            if defense >= enemy.attacksDMG[randomNumber]:
                enemy.hp -= enemy.hp//5
                print("Odbiles atak wroga!")
            else:
                self.hp -= enemy.attacksDMG[randomNumber]-defense
            options = self.attacks
            Game.print_screen(text, self.hp,
                              self.mana, self.money, options, self.currentLocation)
            # player turn
            at = input()
            defense = self.attack(at, enemy, GAME.story)
            if defense == None:
                return None

            if enemy.hp <= 0:
                print(enemy.defeated)
                coins = Game.drop_money(hp_for_money)
                PLAYER.money += coins
                coins = "\033[93m" + str(coins) + "\033[0m"
                print("Za udana walke otrzymujesz ", coins, " pieniedzy!")
                wait = input()
                break
            if self.hp <= 0:
                print("UMARLES! (Twoja postac zostanie usunieta za chwile)")
                wait = input()
                self.deleteCharacter()
                sys.exit(1)

            text = enemy.getDMG[randomNumber]
            print(text)
            wait = input()
        return 13

    def manaRegen(self):
        randomNumber = randint(10, 22)
        if self.clas == "Mag":
            clasMultiplicator = 2
        elif self.clas == "Lucznik":
            clasMultiplicator = 1
        else:
            clasMultiplicator = 0.5
        self.mana += int(randomNumber * clasMultiplicator)
        if self.mana > 100:
            self.mana = 100

    def skills(self):
        opt = ["Leczenie", "Ulepszenie Broni",
               "Wytworzenie monet", "Storzenie broni *rare*"]
        print("Twoje umiejetnosci: ")
        print("1. ", opt[0])
        print("2. ", opt[1])
        print("3. ", opt[2])
        print("4. ", opt[3])
        print("\nCo chcesz zrobic?")

        try:
            dec = (Game.which_option(input(), opt))-1
        except:
            return

        if dec == None:
            return

        randomNumber = randint(5, 20)
        self.mana -= 25
        if self.mana < 0:
            self.mana += 25
            print("Masz za malo many!")
            wait = input()
            return

        if dec == 0:
            self.hp += randomNumber
            if self.hp > 100:
                self.hp = 100
            print("Zostales uleczony i twoje zdrowie wynosi ", self.hp)
            wait = input()
            return
        if dec == 1:
            for item in self.eq.items():
                self.eq[item[0]][0] += randomNumber // 4
                self.eq[item[0]][1] += randomNumber // 4

            print("Ulepszyles i naprawiles swoja bron")
            wait = input()
            return
        if dec == 2:
            self.money += randomNumber
            print("Udalo ci sie wyczarowac ", randomNumber, " monet!")
            wait = input()
            return
        if dec == 3:
            if self.isKox == True:
                self.eq["Giga Bronka"] = [1000, 100]
                print("JAK?!")
                wait = input()
                return
            print("Nie udalo ci sie. Jestes jeszcze za slaby!")


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
    text, directions, options, optionsType = Game.getInformations(GAME, PLAYER)

    if GAME.story[PLAYER.currentLocation]["fightingLocation"] and PLAYER.currentLocation not in PLAYER.seenFightingLocation:

        PLAYER.manaRegen()

        text1 = GAME.story[PLAYER.currentLocation]['text1']
        print(text1)
        while True:
            state = PLAYER.fight(PLAYER, GAME)
            PLAYER.seenFightingLocation.append(PLAYER.currentLocation)
            if state == None:
                PLAYER.currentLocation = "EAGLE TOWN"
            text, directions, options, optionsType = Game.getInformations(
                GAME, PLAYER)
            break

    Game.print_screen(text, PLAYER.hp,
                      PLAYER.mana, PLAYER.money, options, PLAYER.currentLocation)

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
            Game.print_help()
            print("Co chcesz zrobić?")
            decision = input()
            continue
        if decision.lower() == "skills":
            PLAYER.skills()
            print("Uzyles umiejetnosci! Gdzie chcesz teraz isc?")
            decision = input()
            continue
        if Game.which_option(decision, options) == None:
            print("Nie rozumiem cie...")
            decision = input()
            continue

        PLAYER.makeMove(decision, options, optionsType, directions, GAME)
        flag = False


def main():
    Game.terminal_size()

    with open("story.json") as f:
        story = json.load(f)

    PLAYER = Character()
    PLAYER.save_character()
    GAME = Game(story)

    while True:
        play(PLAYER, GAME)


if __name__ == '__main__':
    main()
