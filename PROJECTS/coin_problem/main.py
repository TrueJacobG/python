# 500, 200 , 100, 50, 20, 10, 5, 2, 1
# how many bills/coins do you need to create that number
# min

def how_many_coins(number):
    m = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    result = 0
    x = 0
    while number != 0:
        if number - m[x] >= 0:
            result += 1
            number -= m[x]
        else:
            x += 1
    return result


if __name__ == '__main__':
    print(how_many_coins(123))
