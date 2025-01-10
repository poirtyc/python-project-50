import argparse
from .generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output", metavar="FORMAT")
    args = parser.parse_args()
    data = generate_diff(args.first_file, args.second_file)
    print(data)


if __name__ == "__main__":
    main()
