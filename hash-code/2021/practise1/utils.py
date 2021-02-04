def insert_sorted_dict_array(array: list, item: dict, key: str):
    half = 0
    value = item[key]
    temp_array = array
    found = False
    while not found:
        half = round(len(temp_array) / 2)
        half_value = temp_array[half][key]
        if value < half_value:
            temp_array = temp_array[:half]
        elif value > half_value:
            temp_array = temp_array[half:]
        else:
            found = True

    return array[:half] + [item] + array[half:]


def read(file_name: str):
    with open(file_name, 'r') as file:
        lines = file.read().split('\n')

    photos = []
    for i in range(1, int(lines[0]) + 1):
        line = lines[i].split(' ')
        is_horizontal = line[0] == 'H'
        tag_count = int(line[1])
        tags = set(line[2:])
        photos.append({
            'id': i - 1,
            'is_horizontal': is_horizontal,
            'tag_count': tag_count,
            'tags': tags
        })

    return photos


def write(file_name: str, slides: list):
    lines = ''
    lines += f'{str(len(slides))}\n'
    lines += '\n'.join([' '.join([f'{photo["id"]}' for photo in slide]) + '\n' for slide in slides])
    with open(file_name, 'w+') as file:
        file.write(lines)
