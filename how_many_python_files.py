import os

counter = 0

for x, y, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            counter += 1

print(counter)
