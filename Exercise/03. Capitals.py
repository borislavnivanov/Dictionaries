states = input().split(', ')
capitals = input().split(', ')

result = dict(zip(states, capitals))

for state, capital in result.items():
    print(f"{state} -> {capital}")