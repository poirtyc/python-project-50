import json


def load_data(file_path):
    with open(file_path) as file:
        return json.load(file)


def compare_keys(data1, data2):
    return sorted(data1.keys() | data2.keys())


def generate_diff(file1_path, file2_path):
    data1 = load_data(file1_path)
    data2 = load_data(file2_path)

    result = []
    keys = compare_keys(data1, data2)

    for key in keys:
        if key in data1 and key not in data2:
            result.append(f"- {key}: {data1[key]}")
        elif key in data2 and key not in data1:
            result.append(f"+ {key}: {data2[key]}")
        elif data1[key] == data2[key]:
            result.append(f"  {key}: {data1[key]}")
        else:
            result.append(f"- {key}: {data1[key]}")
            result.append(f"+ {key}: {data2[key]}")

    return "{\n  " + "\n  ".join(result) + "\n}"
