# 3085번 사탕 게임
N = int(input())
board = [list(input()) for _ in range(N)]

def cnady():
    global candymax
    # 가로 바뀐거 하나씩 다 체크
    for col in range(N):
        tempmax = 1
        for row in range(N - 1):
            if board[col][row] == board[col][row + 1]:
                tempmax += 1
            else:
                if candymax < tempmax:
                    candymax = tempmax
                tempmax = 1
        if candymax < tempmax:
            candymax = tempmax

    # 세로 바뀐거 하나씩 다 체크
    for row in range(N):
        tempmax = 1
        for col in range(N - 1):
            if board[col][row] == board[col + 1][row]:
                tempmax += 1
            else:
                if candymax < tempmax:
                    candymax = tempmax
                tempmax = 1

        if candymax < tempmax:
            candymax = tempmax

candymax = 0
for i in range(N):
    for j in range(N-1):
        #  바꾸기
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        # 바뀐거 체크
        cnady()
        # 원상복구
        board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
        # # 바꾸기
        board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
        cnady()
        # 원상복구
        board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
print(candymax)