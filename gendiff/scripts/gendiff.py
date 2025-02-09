import argparse

from gendiff.parsers.file_loader import get_dictionary

from .generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f", "--format", help="set format of output", metavar="FORMAT"
    )
    args = parser.parse_args()
    data1 = get_dictionary(args.first_file)
    data2 = get_dictionary(args.second_file)
    return generate_diff(data1, data2)


if __name__ == "__main__":
    print(main())
