# 2468번 안전 영역

N = int(input())
location = [list(map(int, input().split())) for _ in range(N)]
origin = [location[i][:] for i in range(N)]



maxheight = 0
for i in range(N):
    for j in range(N):
        if location[i][j] > maxheight:
            maxheight = location[i][j]


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
def bfs(i, j):
    q = []
    q.append([i, j])
    while q:
        a, b = q.pop(0)
        for i in range(4):
            ni = a + di[i]
            nj = b + dj[i]
            if 0 <= ni < N and 0 <= nj < N and location[ni][nj] != "X":
                location[ni][nj] = "X"
                q.append([ni, nj])

maxsafty = 0
for height in range(maxheight+1):
    for col in range(N):
        for row in range(N):
            if location[col][row] <= height:
                location[col][row] = "X"
    temp = 0
    for col in range(N):
        for row in range(N):
            if location[col][row] != "X":
                temp += 1
                bfs(col, row)

    if temp > maxsafty:
        maxsafty = temp
    location = [origin[x][:] for x in range(N)]

print(maxsafty)



