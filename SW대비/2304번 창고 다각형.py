# 2304번 창고 다각형

N = int(input())
widthmax = 0
heightmax = 0
pillar = []
for i in range(N):
    temp = list(map(int, input().split()))
    if temp[0] > widthmax:
        widthmax = temp[0]
    if temp[1] > heightmax:
        heightmax = temp[1]
    pillar.append(temp)

wearhouse = [[0] * (widthmax + 2) for _ in range(heightmax + 2)]

for i in range(N):
    for col in range(pillar[i][0], pillar[i][0]+1):
        for row in range(heightmax+1, heightmax-pillar[i][1]+1, -1):
            wearhouse[row][col] = 1

for jj in range(len(wearhouse)):
    print(wearhouse[jj])