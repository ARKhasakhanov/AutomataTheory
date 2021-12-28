s = input()
sost = 'q0'

for i in s:
    if sost == 'q0':
        if i == 'A' or i == 'C':
            sost = 'q0'
        elif i == 'B':
            sost = 'q1'
    elif sost == 'q1':
        if i == 'A' or i == 'C':
            sost = 'q2'
        elif i == 'B':
            sost = 'q3'
    elif sost == 'q2':
        sost = ''
    elif sost == 'q3':
        sost = '-'
if sost == '' or sost == 'q2':
    print('YES')
elif sost == '-' or sost == 'q3':
    print('NO')