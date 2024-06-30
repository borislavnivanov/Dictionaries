phonebook = {}
n = 0

while True:
    text = input().split('-')
    if text[0].isdigit():
        n = int(text[0])
        break

    phonebook[text[0]] = text[1]

for _ in range(n):
    name = input()
    if name not in phonebook:
        print(f'Contact {name} does not exist.')
    else:
        print(f'{name} -> {phonebook[name]}')