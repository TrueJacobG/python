import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print("Welcome in my simple game! \n Guess a number from 1 do 100!")

ifWon = False
randomNumber = random.randrange(0, 101)
counter = 1


while ifWon == False:
    try:
        inputNum = int(input("-> "))
    except:
        print(f"{bcolors.FAIL}You have to input a int number!{bcolors.ENDC}")
        continue
    if not inputNum or type(inputNum) != int:
        print(f"{bcolors.FAIL}You have to input a int number!{bcolors.ENDC}")
        continue
    inputNum = int(inputNum)
    if inputNum > randomNumber:
        print(f"{bcolors.OKBLUE}Your number is bigger than my!{bcolors.ENDC}")
        counter += 1
        continue
    elif inputNum < randomNumber:
        print(f"{bcolors.WARNING}Your number is lower than my!{bcolors.ENDC}")
        counter += 1
        continue
    else:
        print(f"{bcolors.OKGREEN}Congrats! You won! You guessed in {counter} tries{bcolors.ENDC}")
        ifWon = True
