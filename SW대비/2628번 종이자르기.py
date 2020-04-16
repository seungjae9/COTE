# 2628번 종이자르기

width, height = map(int, input().split())
N = int(input())
cut = [list(map(int, input().split())) for _ in range(N)]

paper = [[0] * (width) for _ in range(height)]

for i in range(N):
    if cut[i][0] == 0:
        for j in range(cut[i][1]):
            for x in range(width):
                paper[j][x] += 1
    elif cut[i][0] == 1:
        for j in range(height):
            for x in range(cut[i][1], width):
                paper[j][x] += 100

check = {}
for i in range(height):
    for j in range(width):
        if paper[i][j] not in check:
            check[paper[i][j]] = 1
        else:
            check[paper[i][j]] += 1

ans = 0
for val in check.values():
    if val > ans:
        ans = val
print(ans)

