s = input()

flag = True
sost = 'q0'
for i in s:
    if sost == 'q0':
        if i == 'A':
            sost = 'q1'
        else:
            sost = 'q2'
            flag = False
            break
    elif sost == 'q1':
        if i == 'B':
            sost = 'q3'
        else:
            sost = 'q2'
            flag = False
            break
    elif sost == 'q3':
        if i == 'C' or i == 'A':
            sost = 'q4'
        else:
            sost = 'q2'
            flag = False
            break
    elif sost == 'q4':
        if i == 'C' or i == 'A':
            sost = 'q3'
        elif i == 'B':
            sost = 'q5'
            break
        elif i == 'D' or i == 'E':
            sost = 'q2'
            flag = False
            break
if flag:
    print('YES')
else:
    print('NO')