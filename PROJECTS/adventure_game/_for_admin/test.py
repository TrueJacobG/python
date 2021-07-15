import json

with open("storycopy.json") as f:
    story = json.load(f)

# 67


def countMoves(story):
    moves = 0
    for city in story.values():
        try:
            for action in city["optionsType"]:
                if action == "move":
                    moves += 1
        except:
            pass
    return moves


print(countMoves(story))
