def main():
    n = int(input())
    if n >= 0:
        print(n)
        return

    n = list(str(n))

    if n[len(n)-2] > n[len(n)-1]:
        n[len(n)-2] = ""
    else:
        n[len(n)-1] = ""

    if "".join(n) == "-0":
        print(0)
        return
        
    print("".join(n))


if __name__ == '__main__':
    main()
