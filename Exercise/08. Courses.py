courses = {}

while True:
    reg = input().split(' : ')
    if reg[0] == 'end':
        break

    if reg[0] not in courses:
        courses[reg[0]] = [reg[1]]
    else:
        courses[reg[0]].append(reg[1])

for key, value in courses.items():
    print(f'{key}: {len(value)}')
    for name in value:
        print(f'-- {name}')