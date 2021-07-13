from math import floor

songs, duration = [int(x) for x in input().split()]
times = [int(x) for x in input().split()]

jokes = 0
while songs:
    songs -= 1
    duration -= times.pop()
    if duration < 0:
        songs += 1
        break
    duration -= 5
    jokes += 1
    if duration < 0:
        jokes -= 1
        break
    duration -= 5
    jokes += 1
    if duration < 0:
        jokes -= 1
        break
    if songs == 0:
        jokes += floor(duration / 5)

if songs != 0:
    print(-1)
else:
    print(jokes)
