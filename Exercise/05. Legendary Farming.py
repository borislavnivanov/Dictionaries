farmed = {"shards": 0, "fragments": 0, "motes": 0}
key_materials = {"shards": 'Shadowmourne', "fragments": 'Valanyr', "motes": 'Dragonwrath'}
obtained = str

while True:
    break_flag = False
    text = input().lower().split(' ')
    for key in range(1, len(text) + 1, 2):
        value = key - 1
        if text[key] not in farmed:
            farmed[text[key]] = int(text[value])
        else:
            farmed[text[key]] += int(text[value])
        if text[key] in key_materials and farmed[text[key]] >= 250:
            obtained = text[key]
            farmed[text[key]] -= 250
            break_flag = True
            break
    if break_flag:
        break

print(f'{key_materials[obtained]} obtained!')
for key, value in farmed.items():
    if key in key_materials.keys():
        print(f'{key}: {value}')
for key, value in farmed.items():
    if key not in key_materials.keys():
        print(f'{key}: {value}')