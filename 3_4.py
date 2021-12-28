s = input()

flag = True
sost = 'q0'
for i in s:
    if sost == 'q0':
        if i == 'A' or i == 'B':
            sost = 'q1'
        else:
            sost = 'q2'
            flag = False
            break
    elif sost == 'q1':
        if i == 'C':
            sost = 'q3'
        else:
            sost = 'q2'
            flag = False
            break
    elif sost == 'q3':
        if i == 'B' or i == 'A' or i == 'E':
            sost = 'q4'
        else:
            sost = 'q2'
            flag = False
            break
    elif sost == 'q4':
        if i == 'A' or i == 'B' or i == 'E':
            sost = 'q3'
        elif i == 'D':
            sost = 'q5'
        elif i == 'C':
            sost = 'q2'
            flag = False
            break
    elif sost == 'q5':
        if i == 'D':
            sost = 'a4'
        else:
            break
if flag:
    print('YES')
else:
    print('NO')