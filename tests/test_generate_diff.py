from pathlib import Path

import pytest

from gendiff.scripts.generate_diff import generate_diff

@pytest.fixture
def generate_diff_func():
    return generate_diff


def get_path_files(filename):
    return Path(__file__).parent / 'test_data' / filename


def read_file(filename):
    try:
        return get_path_files(filename).read_text()
    except FileNotFoundError:
        pytest.fail(f"File {filename} not found")


def test_generate_diff(generate_diff_func):
    file1 = get_path_files("file1.json")
    file2 = get_path_files("file2.json")
    after_file = read_file("after.txt")

    actual = generate_diff_func(str(file1), str(file2))

    assert actual == after_file