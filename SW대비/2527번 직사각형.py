# 2527번 직사각형
# 시간초과


for i in range(1):
    rectangle = list(map(int, input().split()))

    board = [[0] * 50000 for _ in range(50000)]
    A = rectangle[0:4]
    B = rectangle[4:]

    for j in range(A[1]+1, A[3]+2):
        for x in range(A[0], A[2]+1):
            board[50000 - j][x] = 1

    for j in range(B[1]+1, B[3]+2):
        for x in range(B[0], B[2]+1):
            board[50000-j][x] += 1


    res = [0, 0, 0, 0]

    stoppoint = 0
    for i in range(A[1] + 1, A[3]):
        for j in range(A[0] + 1, A[2]):
            if board[50000 - i -1][j] == 2:
                res[0] = 1
                stoppoint = 1
                break
        if stoppoint == 1:
            break

    # 선분 검증
    if res[0] == 0:
        line = 0
        # 아래
        for i in range(A[0] + 1, A[2]):
            if board[50000 - A[1] -1][i]== 2:
                res[1] = 1
                break
                # line += 1

                # 3,2    9,8
        # 오른쪽
        for i in range(A[1] + 1, A[3]):
            if board[50000-i-1][A[2]] == 2:
                res[1] = 1
                break
                # line += 1

        # 위쪽
        for i in range(A[0] + 1 , A[2]):
            if board[50000-A[3]- 1][i] == 2:
                res[1] = 1
                break
                # line += 1

        # 왼쪽
        for i in range(A[1] + 1, A[3]):
            if board[10000 - i - 1][A[0]] == 2:
                res[1] = 1
                break
                # line += 1
    # 모서리 검증
    if res[0] == 0 and res[1] == 0:
        if board[50000 - A[1] - 1][A[0]] == 2 or board[50000 - A[1] - 1][A[2]] == 2 or board[50000 - A[3] - 1][A[0]] == 2 or board[50000 - A[3] - 1][A[2]] == 2:
            res[2] = 1

    # 아무것도 없는거 검증
    if res[0] == 0 and res[1] == 0 and res[2] == 0:
        res[3] = 1


    print(res)





