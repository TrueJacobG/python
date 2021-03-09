def attackFirstly(robot_1, robot_2):
    if robot_1["speed"] > robot_2["speed"]:
        return 1
    elif robot_1["speed"] < robot_2["speed"]:
        return 2
    else:
        return 1


def dmg(robot, tactics, count):
    try:
        return tactics[robot["tactics"][count]]
    except:
        return 0


def winnerf(robot_1, robot_2, count):
    if count == 1:
        winnerName = robot_1["name"]
        return f"{winnerName} has won the fight."
    elif count == 2:
        winnerName = robot_2["name"]
        return f"{winnerName} has won the fight."
    else:
        return "The fight was a draw."


def fight(robot_1, robot_2, tactics):
    start = attackFirstly(robot_1, robot_2)
    alive = True
    c1 = 0
    c2 = 0
    if start == 1:
        while alive:
            if dmg(robot_1, tactics, c1) == 0 and dmg(robot_2, tactics, c2) == 0:
                if robot_1["health"] > robot_2["health"]:
                    winner = 1
                elif robot_2["health"] > robot_1["health"]:
                    winner = 2
                else:
                    winner = 0
                alive = False
                break
            robot_2["health"] = robot_2["health"] - \
                dmg(robot_1, tactics, c1)
            c1 += 1
            if robot_2["health"] <= 0:
                alive = False
                winner = 1
                break

            robot_1["health"] = robot_1["health"] - \
                dmg(robot_2, tactics, c2)
            c2 += 1
            if robot_1["health"] <= 0:
                alive = False
                winner = 2
                break

    if start == 2:
        while alive:
            if dmg(robot_1, tactics, c1) == 0 and dmg(robot_2, tactics, c2) == 0:
                if robot_1["health"] > robot_2["health"]:
                    winner = 1
                elif robot_2["health"] > robot_1["health"]:
                    winner = 2
                else:
                    winner = 0
                alive = False
                break

            robot_1["health"] = robot_1["health"] - \
                dmg(robot_2, tactics, c2)
            c2 += 1
            if robot_1["health"] <= 0:
                alive = False
                winner = 2
                break

            robot_2["health"] = robot_2["health"] - \
                dmg(robot_1, tactics, c1)
            c1 += 1
            if robot_2["health"] <= 0:
                alive = False
                winner = 1
                break

    return winnerf(robot_1, robot_2, winner)


robot_1 = {"name": "Rocky", "health": 100, "speed": 20,
           "tactics": ["punch", "punch", "laser", "missile"]}

robot_2 = {"name": "Missile Bob", "health": 100, "speed": 21,
           "tactics": ["missile", "missile", "missile", "missile"]}

tactics = {"punch": 20, "laser": 30, "missile": 35}

print(fight(robot_1, robot_2, tactics))  # bob

robot_1 = {"name": "Rocky", "health": 200, "speed": 20,
           "tactics": ["punch", "punch", "laser", "missile"]}
robot_2 = {"name": "Missile Bob", "health": 100, "speed": 21,
           "tactics": ["missile", "missile", "missile", "missile"]}
tactics = {"punch": 20, "laser": 30, "missile": 35}
print(fight(robot_1, robot_2, tactics))  # rocky
