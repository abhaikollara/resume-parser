import sys
from pprint import pprint

from utils import read_text
from parser import Parser


def main():
    try:
        path = sys.argv[1]
    except IndexError:
        print("Error: No input files")
        sys.exit()

    text = read_text(path)
    # print
    p = Parser()
    info = p.parse(text)
    pprint(info)


if __name__ == '__main__':
    main()
