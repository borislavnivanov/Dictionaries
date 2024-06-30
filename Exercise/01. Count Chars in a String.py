text = input()
chars = {}

for char in text:
    if char != ' ':
        if char not in chars:
            chars[char] = 0
        chars[char] += 1

for char, value in chars.items():
    print(f'{char} -> {value}')