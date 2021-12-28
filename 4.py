def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


avtomat = {'q0': ['q1', 'q2'],
           'q1': ['q2', 'q1'],
           'q2': ['q0', 'q3'],
           'q3': ['q4', 'q3'],
           'q4': ['q5', 'q3'],
           'q5': ['q5', 'q3']}
k0 = ['q0', 'q1', 'q2']
k = ['q3', 'q4', 'q5']

for value in avtomat.values():
    for i in range(2):
        if value[i] == 'q3' or value[i] == 'q4' or value[i] == 'q5':
            for j in k0:
                if get_key(avtomat, value) == j:
                    k1 = [j]
                    del k0[k0.index(j)]
                    break

for value in avtomat.values():
    for i in range(2):
        if value[i] == 'q0' or value[i] == 'q1' or value[i] == 'q2':
            for j in k:
                if get_key(avtomat, value) == j:
                    k2 = [j]
                    del k[k.index(j)]
                    break

for value in avtomat.values():
    for i in range(2):
        if value[i] == 'q2':
            for j in k0:
                if get_key(avtomat, value) == j:
                    k3 = [j]
                    del k0[k0.index(j)]
        break

print(k0)
print(k1)
print(k3)
print(k)

avtomat = {k0[0] : ['q1', 'q2'],
           k3[0] : ['q2', 'q1'],
           k1[0] : ['q0', 'q3'],
           ''.join(k) : [''.join(k), ''.join(k)]}
print(avtomat)