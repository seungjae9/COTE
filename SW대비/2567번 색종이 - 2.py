# 2567번 색종이 - 2

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

board = [[0] * 102 for _ in range(102)]

for i in range(N):
    for x in range(paper[i][1], paper[i][1]+10):
        for j in range(paper[i][0], paper[i][0]+10):
            board[x][j] = 1

res = 0
for i in range(1, 102):
    for j in range(1, 102):
        if board[i][j] == 1:
            if board[i - 1][j] == 0:
                res += 1
            if board[i + 1][j] == 0:
                res += 1
            if board[i][j - 1] == 0:
                res += 1
            if board[i][j + 1] == 0:
                res += 1

print(res)



