from random import randint, randrange, choice
from words import words

def get_word():
    word = choice(words)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    gussed_letters = []
    gussed_words = []
    tries = 6
    print("HANGMAN! PLANTS EDITION  0.1!")
    print("You have ", display_hangman(tries), "tries")
    print(word_completion, "\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or a word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in gussed_letters:
                print("You printed this before!", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                gussed_letters.append(guess)
            else:
                print("You guessed a letter! GJ!")
                gussed_letters.append(guess)
                word_as_list = list(word_completion)
                indexes = [i for i, letter in enumerate(word) if letter == guess]
                for index in indexes:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)  
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in gussed_words:
                print("You printed it before!")
            elif guess != word:
                print("It's not a correct word.")
                tries -= 1
                gussed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess!")
        print(display_hangman(tries))
        print(word_completion, "\n")

    if guessed:
        print("Congrats! You win! The word was ", word)
    else:
        print("You lost! The word was ", word)


def display_hangman(tries):
    stages = [
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play again? (Y/N)").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()