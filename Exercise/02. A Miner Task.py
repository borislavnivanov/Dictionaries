
chars = {}

while True:
    resource = input()
    if resource == 'stop':
        break
    quantity = int(input())

    if resource not in chars:
        chars[resource] = 0
    chars[resource] += quantity

for char, value in chars.items():
    print(f'{char} -> {value}')