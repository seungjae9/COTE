# # 14502번 연구소

a, b = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(a)]

origin = [[0] * b for _ in range(a)]
for i in range(a):
    for j in range(b):
        origin[i][j] = board[i][j]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(col, row):
    q = []
    q.append([col, row])
    while q:
        x, y = q.pop(0)
        for i in range(4):
            ni = x + di[i]
            nj = y + dj[i]
            if 0 <= ni < a and 0 <= nj < b and board[ni][nj] == 0:
                board[ni][nj] = 2
                q.append([ni, nj])


def npr(n, k, N, s, wall):
    global maxvirus
    if n == k:
        newall = []
        for x in range(3):
            newall.append(wall[p[x]-1])
            board[wall[p[x]-1][0]][wall[p[x]-1][1]] = 1

        for col in range(a):
            for row in range(b):
                if board[col][row] == 2:
                    bfs(col, row)

        temp = 0
        for search in range(a):
            for search2 in range(b):
                if board[search][search2] == 0:
                    temp += 1

        if maxvirus < temp:
            maxvirus = temp

        for origin1 in range(a):
            for origin2 in range(b):
                board[origin1][origin2] = origin[origin1][origin2]

    else:
        for i in range(s, N):
            if used[i] == 0:
                used[i] = 1
                p[n] = i + 1
                npr(n+1, k, N, i, wall)
                used[i] = 0

    return maxvirus

wall = []
for i in range(a):
    for j in range(b):
        if board[i][j] == 0:
            wall.append([i, j])


maxvirus = 0
used = [0] * len(wall)
p = [0] * 3
npr(0, 3, len(wall), 0, wall)

print(maxvirus)