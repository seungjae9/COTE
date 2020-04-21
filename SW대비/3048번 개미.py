# 3048번 개미

N1, N2 = map(int, input().split())
groupA = input()
groupB = input()
T = int(input())

ant = list(groupA[::-1] + groupB)
for i in range(T):
    tempA = []
    tempB = []
    for j in range(N1+N2 - 1):
        if ant[j] in groupA and ant[j+1] in groupB:
            tempA.append(ant[j])
            tempB.append(ant[j+1])
    for x in range(len(tempA)):
        changeA = ant.index(tempA[x])
        changeB = ant.index(tempB[x])
        ant[changeA], ant[changeB] = ant[changeB], ant[changeA]


print("".join(map(str, ant)))
