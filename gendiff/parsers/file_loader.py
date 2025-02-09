import json

import yaml


def parse_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def parse_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


def get_dictionary(file_path):
    file_format = file_path.split('.')[1]
    parser = {
        "json": parse_json,
        "yaml": parse_yaml,
        "yml": parse_yaml,
    }

    if file_format not in parser:
        raise ValueError(f'Unsuported format {file_format}')

    return parser[file_format](file_path)
