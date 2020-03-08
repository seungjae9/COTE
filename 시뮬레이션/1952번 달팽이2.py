# 1952번 달팽이2
# 못풀었음 아직

M, N = map(int, input().split())
board = [[0] * N for _ in range(M)]

check = 0
number = 1

dhfmsWHr = N
dkfofh = M
while check != M * N:


    for i in range(dhfmsWHr):
        board[0][i] = number
        number += 1
    dkfofh += 1

    for i in range(dkfofh):
        board[i][dhfmsWHr] = number
        number += 1
    dhfmsWHr -=1

    for i in range(-dhfmsWHr-1, -1, -1):
        board[i][dkfofh] = number
        number +=1
    dkfofh -= 1

    if check == M * N:
        break