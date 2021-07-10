
def main():
    n = input()
    if n[0] != "1":
        return "NO"
    if n.find("444") != -1:
        return "NO"
    for i in range(len(n)):
        if n[i] != "1":
            if n[i] != "4":
                return "NO"
    return "YES"


if __name__ == "__main__":
    print(main())
