str = 'nppnnpnppppnnppnnpppnn'
sost = 's1'
result = ''
s1count = 0
takt = 0
taktB = []
firstSOSTarray = [0, 0, 0, 0, 0, 0]
for i in str:
    takt += 1
    if sost == 's1':
        firstSOSTarray.insert(0, 1)
        if i == 'n':
            sost = 's2'
            result += 'a'
            s1count += 1
        else:
            sost = 's1'
            result += 'y'
    elif sost == 's2':
        firstSOSTarray.insert(1, 1)
        if i == 'n':
            sost = 's3'
            result += 'a'
        else:
            sost = 's2'
            result += 'b'
            taktB.append(takt)
    elif sost == 's3':
        firstSOSTarray.insert(2, 1)
        if i == 'n':
            sost = 's1'
            result += 'b'
        else:
            sost = 's4'
            result += 'a'
    elif sost == 's4':
        firstSOSTarray.insert(3, 1)
        if i == 'n':
            sost = 's5'
            result += 'a'
        else:
            sost = 's4'
            result += 'a'
    elif sost == 's5':
        firstSOSTarray.insert(4, 1)
        if i == 'n':
            sost = 's5'
            result += 'a'
        else:
            sost = 's6'
            result += 'b'
    elif sost == 's6':
        firstSOSTarray.insert(5, 1)
        if i == 'n':
            sost = 's3'
            result += 'b'
        else:
            sost = 's2'
            result += 'y'
print(result)

print('A')
print(result.count('a'))
print('-----------------')

print('Б')
print(result.count('abb'))
print('-----------------')

print('В')
print(s1count)
print('-----------------')

print('Г')
if result[9] == 'a' and result[19] == 'a' and result[29] == 'a':
    print('Yes')
else:
    print('No')
print('-----------------')

print('Д')
countA = 0
maxA = 0
for i in result:
    if i == 'a':
        countA += 1
        maxA = countA
    else:
        countA = 0
print(maxA)
print('-----------------')

print('Е')
print(taktB[0])
print('-----------------')

print('Ж')
if firstSOSTarray.count(1) == 6:
    print('Yes')
else:
    print('No')
print('-----------------')

print('З')
countA = 0
countB = 0
countY = 0
for i in result:
    if i == 'a':
        countA += 1
    elif i == 'b':
        countB += 1
    elif i == 'y':
        countY += 1
print('\n','A =', countA,'\n','B =',countB,'\n','Y =',countY)
print('-----------------')

