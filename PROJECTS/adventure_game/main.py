import json
from os import path


def createCharacter():
    if not path.isfile("character.json"):
        with open("character_model.json") as f:
            intro = json.load(f)

        with open("character.json", "w") as f:
            json.dump(intro, f)


def play(story, cur_L):
    print(story[cur_L]["text"])
    decision = input()


def main():
    createCharacter()

    with open("story.json") as f:
        story = json.load(f)

    with open("character.json") as f:
        character = json.load(f)

    while True:
        play(story, character["currentLocation"])


if __name__ == '__main__':
    main()
