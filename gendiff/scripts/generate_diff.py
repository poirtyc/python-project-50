import json


def load_data(file_path):
    with open(file_path) as file:
        return json.load(file)


def compare_keys(data1, data2):
    return sorted(data1.keys() | data2.keys())


def format_diff(key, data1, data2):
    if key in data1 and key not in data2:
        return f"- {key}: {data1[key]}"
    if key in data2 and key not in data1:
        return f"+ {key}: {data2[key]}"
    if data1[key] == data2[key]:
        return f"  {key}: {data1[key]}"
    return f"- {key}: {data1[key]}\n  + {key}: {data2[key]}"


def generate_diff(file1_path, file2_path):
    data1 = load_data(file1_path)
    data2 = load_data(file2_path)

    keys = compare_keys(data1, data2)
    result = [format_diff(key, data1, data2) for key in keys]

    return "{\n  " + "\n  ".join(result) + "\n}"
