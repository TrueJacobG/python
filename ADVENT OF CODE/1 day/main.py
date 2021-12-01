def main():
    arr = []
    prevSum = 0
    counter = 0
    with open("input.txt", "r") as f:
        for line in f.readlines():
            arr.append(int(line))

    for i in range(2, len(arr)):
        if (arr[i-2] + arr[i-1] + arr[i]) > prevSum:
            counter += 1
        prevSum = arr[i-2] + arr[i-1] + arr[i]

    print(counter)


if __name__ == '__main__':
    main()
