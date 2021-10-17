import json

with open("items.json") as f:
    # json to dict
    fileDICT = json.load(f)

print(fileDICT)

# change
fileDICT["age"] = 20

# from dict to json file
with open("itemsNew.json", "w") as f:
    # indent -> tabs, spaces, 4 == normal
    json.dump(fileDICT, f, indent=4)


# dict to json
fileJSON = json.dumps(fileDICT, indent=4, sort_keys=True)
print(fileJSON)
