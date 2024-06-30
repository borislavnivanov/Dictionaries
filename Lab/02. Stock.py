elements = input().split(' ')
searched = input().split(' ')
table = {}
for i in range(0, len(elements), 2):
    table[elements[i]] = int(elements[i + 1])

for req in searched:
    if req in table:
        print(f'We have {table[req]} of {req} left')
    else:
        print(f'Sorry, we don\'t have {req}')