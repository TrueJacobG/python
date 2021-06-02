
def main():
    s = str(input())
    if "H" in s or "Q" in s or "9" in s:
        return("YES")
    return("NO")


if __name__ == '__main__':
    print(main())
