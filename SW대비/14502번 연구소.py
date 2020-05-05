# # 14502번 연구소
#
# # 조합으로 벽 세우는데 구하기(0, 0, 0 인데 좌표 찾아서 조합 3개 구하기)
# # 벽세우고 bfs 돌리기

a, b = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(a)]


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

    for xxx in range(len(board)):
        print(board[xxx])
    print()
def npr(n, k, N, s, wall):
    if n == k:
        newall = []
        for x in range(3):
            newall.append(wall[p[x]-1])
            board[wall[p[x]-1][0]][wall[p[x]-1][1]] = 1

        for col in range(a):
            for row in range(b):
                if board[col][row] == 2:
                    bfs(col, row)

        for x in range(3):
            board[wall[p[x]-1][0]][wall[p[x]-1][1]] = 0


    else:
        for i in range(s, N):
            if used[i] == 0:
                used[i] = 1
                p[n] = i + 1
                npr(n+1, k, N, i, wall)
                used[i] = 0

wall = []
for i in range(a):
    for j in range(b):
        if board[i][j] == 0:
            wall.append([i, j])


used = [0] * len(wall)
p = [0] * 3
npr(0, 3, len(wall), 0, wall)

