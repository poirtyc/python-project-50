import json


def load_data(file_path):
    with open(file_path) as file:
        return json.load(file)


def compare_keys(data1, data2):
    return sorted(data1.keys() | data2.keys())


def format_diff(key, data1, data2):
    if key in data1 and key in data2:
        if data1[key] == data2[key]:
            return f"  {key}: {data1[key]}"
        return [f"- {key}: {data1[key]}", f"+ {key}: {data2[key]}"]
    elif key in data1:
        return f"- {key}: {data1[key]}"
    else:
        return f"+ {key}: {data2[key]}"


def generate_diff(file1_path, file2_path):
    data1 = load_data(file1_path)
    data2 = load_data(file2_path)

    result = []
    for key in compare_keys(data1, data2):
        formatted = format_diff(key, data1, data2)
        if isinstance(formatted, list):
            result.extend(formatted)
        else:
            result.append(formatted)

    return "{\n  " + "\n  ".join(result) + "\n}"
