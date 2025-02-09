import pytest

from gendiff.parsers.file_loader import get_dictionary


def test_get_dictionary():
    assert get_dictionary(
        '/Users/dmitriy/Desktop/projects/python-project-50/tests/fixtures/file1.json'
    ) == {
        'host': 'hexlet.io',
        'timeout': 50,
        'proxy': '123.234.53.22',
        'follow': False
    }

    assert get_dictionary(
        '/Users/dmitriy/Desktop/projects/python-project-50/tests/fixtures/file1.yaml'
    ) == {
        'host': 'hexlet.io',
        'timeout': 50,
        'proxy': '123.234.53.22',
        'follow': False
    }


def test_get_dictionary_with_miss():
    with pytest.raises(ValueError, match='Unsuported format'):
        get_dictionary(
            "/Users/dmitriy/Desktop/projects/python-project-50/tests/fixtures/file1.jso"
        )