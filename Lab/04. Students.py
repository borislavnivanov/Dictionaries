students = {}
course = ''

while True:
    text = input()
    if ':' not in text:
        course = text.replace('_',' ')
        break

    lst = text.split(':')
    students[lst[0] + ' - ' + lst[1]] = lst[2]

print('\n'.join([x for x in students if students[x] == course]))