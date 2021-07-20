
def isPrime(n):
    for number in range(2, (n//2)+1):
        if n % number == 0:
            return False
    return True


def main():
    n, m = [int(x) for x in input().split()]

    if not isPrime(m):
        print("NO")
        return

    for number in range(n+1, m+1):
        if isPrime(number) and number != m:
            print("NO")
            return

    print("YES")


if __name__ == "__main__":
    main()
