import argparse

parser = argparse.ArgumentParser(description="-h to see that")

# usage python3 main.py -Path /sciezka/taka -Number 3
parser.add_argument("-Path", metavar="path", type=str)
parser.add_argument("-Number", metavar="number", type=int)

# usage python3 main.py /sciezka/taka 3
# parser.add_argument("Path", metavar="path", type=str)
# parser.add_argument("Number", metavar="number", type=int)


args = parser.parse_args()

for _ in range(args.Number):
    print(args.Path)
