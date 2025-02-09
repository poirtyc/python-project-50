def generate_diff(data1, data2):
    compare_keys = sorted(data1.keys() | data2.keys())

    arr = []
    for key in compare_keys:
        if key not in data2:
            arr.append(f'- {key}: {data1[key]}')
        elif key not in data1:
            arr.append(f'+ {key}: {data2[key]}')
        elif data1[key] != data2[key]:
            arr.append(f'- {key}: {data1[key]}')
            arr.append(f'+ {key}: {data2[key]}')
        else:
            arr.append(f'  {key}: {data1[key]}')
    return f'{{\n  {"\n  ".join(arr)}\n}}'