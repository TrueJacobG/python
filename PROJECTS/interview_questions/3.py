# własna funkcja sortująca

old_list = [1, 5, 3, 6, 8, 9, 3, 7, 9, 4]

new_list = []

while old_list:
    minimum = old_list[0]
    maximum = old_list[len(old_list)-1]

    for x in old_list:
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    old_list.remove(minimum)

print(new_list)
