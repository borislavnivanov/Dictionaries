data = {}

while True:
    text = input().split(' -> ')
    if text[0] == 'End':
        break
    if text[0] not in data:
        data[text[0]] = []
    if text[1] not in data[text[0]]:
        data[text[0]].append(text[1])

for key, value in data.items():
    print(key)
    for name in value:
        print(f'-- {name}')