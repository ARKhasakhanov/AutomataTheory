s = input()
sost = 'q0'


for i in s:
    if sost == 'q0':
        if i == 'A':
            sost = 'q1'
        elif i == 'B' or i == 'C' or i == 'D' or i == 'E':
            sost = 'q2'
    elif sost == 'q1':
        if i == 'B' or i == 'D' or i == 'A':
            sost = 'q3'
        elif i == 'C' or i == 'E':
            sost = 'q2'
    elif sost == 'q3':
        if i == 'A' or i == 'C':
            sost = 'q4'
        elif i == 'B' or i == 'D' or i == 'E':
            sost = 'q2'
    elif sost == 'q4':
        if i == 'E':
            sost = 'q5'
        elif i == 'A' or i == 'B' or i == 'C' or i == 'D':
            sost = 'q2'

if sost == 'q5':
    print('YES')
elif sost == 'q2' or len(sost) > 4:
    print('NO')