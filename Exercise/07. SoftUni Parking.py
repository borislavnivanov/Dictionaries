def register_user(username: str, license_plate: str):
    if username in register:
        print(f'ERROR: already registered with plate number {register[username]}')
    else:
        register[username] = license_plate
        print(f'{username} registered {license_plate} successfully')


def unregister_user(username: str):
    if username in register.keys():
        register.pop(username)
        print(f'{username} unregistered successfully')
    else:
        print(f'ERROR: user {username} not found')


register = {}
n = int(input())

for _ in range(n):
    text = input().split()

    if text[0] == 'register':
        register_user(text[1], text[2])
    else:
        unregister_user(text[1])

for key, value in register.items():
    print(f'{key} => {value}')