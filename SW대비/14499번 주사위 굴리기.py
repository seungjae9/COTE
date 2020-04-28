# 14499번 주사위 굴리기

N, M, x, y, k = map(int, input().split())
board = [[0] * M for _ in range(N)]
number = [list(map(int, input().split())) for _ in range(N)]
direction = list(map(int, input().split()))

for j in range(N):
    for t in range(M):
        board[j][t] = number[j][t]


dice = [0, 0, 0, 0, 0, 0]
res=[]
for case in range(k):
    if direction[case] == 4:
        if x + 1 <= N-1:
            x += 1
            if board[x][y] == 0:
                board[x][y] = dice[4]
            else:
                dice[4] = board[x][y]
                board[x][y] = 0
            dice[0], dice[2], dice[4], dice[5] = dice[5], dice[0], dice[2], dice[4]
            res.append(dice[2])
    elif direction[case] == 1:
        if y + 1 <= M - 1:
            y += 1
            if board[x][y] == 0:
                board[x][y] = dice[3]
            else:
                dice[3] = board[x][y]
                board[x][y] = 0
            dice[1], dice[2], dice[3], dice[5] = dice[5], dice[1], dice[2], dice[3]
            res.append(dice[2])
    elif direction[case] == 3:
        if x - 1 >= 0:
            x -= 1
            if board[x][y] == 0:
                board[x][y] = dice[0]
            else:
                dice[0] = board[x][y]
                board[x][y] = 0
            dice[0], dice[2], dice[4], dice[5] = dice[2], dice[4], dice[5], dice[0]
            res.append(dice[2])
    elif direction[case] == 2:
        if y - 1 >= 0:
            y -= 1
            if board[x][y] == 0:
                board[x][y] = dice[1]
            else:
                dice[1] = board[x][y]
                board[x][y] = 0
            dice[1], dice[2], dice[3], dice[5] = dice[2], dice[3], dice[5], dice[1]
            res.append(dice[2])
for i in range(len(res)):
    print(res[i])