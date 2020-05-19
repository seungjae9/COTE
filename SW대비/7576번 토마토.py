# 7576번 토마토
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

def bfs(check):
    while check:
        temp = []
        for v in check:
            a, b = v[0], v[1]
            for i in range(4):
                ni = a + di[i]
                nj = b + dj[i]
                if 0 <= ni < N and 0 <= nj < M and tomato[ni][nj] == 0:
                    temp.append([ni, nj])
                    tomato[ni][nj] = tomato[a][b] + 1
        check = temp
check = []
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            check.append([i, j])

bfs(check)

maxtime = 0
stop = 0
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            stop = 1
            break
        else:
            if tomato[i][j] > maxtime:
                maxtime = tomato[i][j]
    if stop == 1:
        maxtime = 0
        break

print(maxtime-1)