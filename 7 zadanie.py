import random

E = random.choice([True, False])
print('E =', E)
items = {0: E or E,
         1: E and E,
         2: E,
         3: not E}
stritems = ['E or E', 'E and E', 'E', 'not E']

a = random.randint(1, 4)
c = random.randint(0, 1)

if a == 1:
    b1 = random.randint(0, 3)
    b2 = random.randint(0, 3)
    E = items[b1] or items[b2]
    strE = stritems[b1] + ' or ' + stritems[b2]
    if c == 1:
        E = not(items[b1] or items[b2])
        strE = 'not (' + stritems[b1] + ' or ' + stritems[b2] + ')'
        print(strE)
        print(E)
    else:
        print(strE)
        print(E)

if a == 2:
    b1 = random.randint(0, 3)
    b2 = random.randint(0, 3)
    E = items[b1] and items[b2]
    strE = stritems[b1] + ' and ' + stritems[b2]
    if c == 1:
        E = not (items[b1] and items[b2])
        strE = 'not (' + stritems[b1] + ' and ' + stritems[b2] + ')'
        print(strE)
        print(E)
    else:
        print(strE)
        print(E)

if a == 3:
    b = random.randint(0, 3)
    E = items[b]
    strE = stritems[b]
    if c == 1:
        E = not (items[b] or not items[b])
        strE = 'not (' + stritems[b] + ' or not ' + stritems[b] + ')'
        print(strE)
        print(E)
    else:
        print(strE)
        print(E)

if a == 4:
    b = random.randint(0, 3)
    E = not items[b]
    strE = 'not ' + stritems[b]
    if c == 1:
        E = not (items[b] and not items[b])
        strE = 'not (' + stritems[b] + ' and not ' + stritems[b] + ')'
        print(strE)
        print(E)
    else:
        print(strE)
        print(E)





