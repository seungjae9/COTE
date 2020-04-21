# 3805번 사탕 게임

N = int(input())
origin = [list(input()) for _ in range(N)]

board = [[0] * N for _ in range(N)]

# 가로 바꾸기
for i in range(N):
    for j in range(N-1):

        for col in range(N):
            for row in range(N):
                board[col][row] = origin[col][row]

        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

        compare1 = 0
        compare2 = 0

        initial = board[i][j]


        check = 1
        for x in range(i, N):
            if x - check >= 0:
                if board[x-check][j] == initial:
                    compare1 += 1
            if x + check <= N - 1:
                if board[x+check][j] == initial:
                    compare2 += 1
            check += 1


        print(compare1 + compare2)



