items = {}
quantities = {}

while True:
    text = input().split(' ')
    if text[0] == 'buy':
        break
    if text[0] not in items:
        items[text[0]] = float(text[1])
        quantities[text[0]] = int(text[2])
    else:
        if items[text[0]] != float(text[1]):
            items[text[0]] = float(text[1])
        quantities[text[0]] += int(text[2])

for item, price in items.items():
    print(f'{item} -> {price * quantities[item]:.2f}')