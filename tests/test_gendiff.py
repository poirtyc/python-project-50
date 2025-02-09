import sys
from unittest.mock import patch

from gendiff.scripts.gendiff import main


def normalize(text):
    lines = text.strip().split("\n")
    lines = [line.strip() for line in lines]
    return "\n".join(sorted(lines))


def test_main():
    expected = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""

    test_args = [
        "gendiff",
        "tests/fixtures/file1.json",
        "tests/fixtures/file2.json",
    ]

    with patch.object(sys, "argv", test_args):
        result = main()

    assert normalize(result) == normalize(expected)