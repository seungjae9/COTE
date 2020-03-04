# 14696번 딱지놀이

result = []
for i in range(int(input())):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    As = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    Bs = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    del A[0]
    del B[0]

    for i in A:
        if i == 4:
            As['A'] += 1
        elif i == 3:
            As['B'] += 1
        elif i == 2:
            As['C'] += 1
        elif i == 1:
            As['D'] += 1
    for i in B:
        if i == 4:
            Bs['A'] += 1
        elif i == 3:
            Bs['B'] += 1
        elif i == 2:
            Bs['C'] += 1
        elif i == 1:
            Bs['D'] += 1

    if As['A'] > Bs['A']:
        result.append('A')
    elif As['A'] < Bs['A']:
        result.append('B')
    elif As['B'] > Bs['B']:
        result.append('A')
    elif As['B'] < Bs['B']:
        result.append('B')
    elif As['C'] > Bs['C']:
        result.append('A')
    elif As['C'] < Bs['C']:
        result.append('B')
    elif As['D'] > Bs['D']:
        result.append('A')
    elif As['D'] < Bs['D']:
        result.append('B')
    elif As['D'] == Bs['D']:
        result.append('D')

for i in result:
    print(i)

# dict = {'A': 1, 'B': 2, 'C': 3}
# for key, val in dict.items():
#     print(key, val)