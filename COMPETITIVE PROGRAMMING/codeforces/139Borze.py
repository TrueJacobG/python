def main():
    s = input()
    return s.replace("--", "2").replace("-.", "1").replace(".", "0")


if __name__ == "__main__":
    print(main())
