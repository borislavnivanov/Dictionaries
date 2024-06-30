products = {}

while True:
    item = input()
    if item == 'statistics':
        break

    key, value = item.split(': ')
    if key not in products:
        products[key] = int(value)
    else:
        products[key] += int(value)


print(f'Products in stock:')
for product, values in products.items():
    print(f'- {product}: {values}')
print(f'Total Products: {len(products.keys())}\nTotal Quantity: {sum(products.values())}')