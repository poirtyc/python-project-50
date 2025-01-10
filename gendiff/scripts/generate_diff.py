import json


def generate_diff(file1_path, file2_path):
    data1 = json.load(open(file1_path))
    data2 = json.load(open(file2_path))

    result = []
    keys = sorted(set(data1.keys()) | set(data2.keys()))

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
