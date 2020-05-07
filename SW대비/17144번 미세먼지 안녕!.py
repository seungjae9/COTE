# 17144번 미세먼지 안녕!

R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]


machine = []
for i in range(R):
    for j in range(C):
        if board[i][j] == -1:
            machine.append([i, j])
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

cnt = 0
while cnt < T:
    b = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if board[i][j] != -1 and board[i][j] != 0:
                dust = board[i][j] // 5
                for x in range(4):
                    ni = i + di[x]
                    nj = j + dj[x]
                    if 0 <= ni < R and 0 <= nj < C and board[ni][nj] != -1:
                        b[ni][nj] += dust
                        board[i][j] -= dust

    for i in range(R):
        for j in range(C):
            board[i][j] += b[i][j]

    b = [[0] * C for i in range(R)]
    for i in range(R):
        for j in range(C):
            if i == machine[0][0] and j != 0 and j != C-1 or i == machine[1][0] and j != 0 and j != C-1:
                board[i][j], b[i][j+1] = 0, board[i][j]
            if i == machine[0][0] and j == C - 1:
                for x in range(machine[0][0], 0, -1):
                    board[x][j], b[x-1][j] = 0, board[x][j]
            if i == machine[1][0] and j == C - 1:
                for x in range(machine[1][0], R-1, 1):
                    board[x][j], b[x+1][j] = 0, board[x][j]
            if i == 0 and j != 0 or i == R - 1 and j != 0:
                board[i][j], b[i][j-1] = 0, board[i][j]
            if i == machine[0][0] and j == 0:
                board[i-1][j] = 0
                for x in range(0, machine[0][0]-1, 1):
                    board[x][j], b[x+1][j] = 0, board[x][j]
            if i == machine[1][0] and j == 0:
                board[i+1][j] = 0
                for x in range(machine[1][0] + 2, R, 1):
                    board[x][j], b[x-1][j] = 0, board[x][j]

    for i in range(R):
        for j in range(C):
            board[i][j] += b[i][j]

    cnt += 1

res = 0
for i in range(R):
    for j in range(C):
       if board[i][j] != -1:
           res += board[i][j]

print(res)
