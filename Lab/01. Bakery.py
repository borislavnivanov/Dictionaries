elements = input().split(' ')
table = {}
for i in range(0, len(elements), 2):
    table[elements[i]] = int(elements[i + 1])

print(table)