# 2527번 직사각형

# rectangle = [list(map(int, input().split())) for _ in range(4)]

                      # ------------
                      # |          |
                      # |          |
                      # ------------
#                         왼아래모, 오아래모, 왼위모, 오위모

for i in range(1):
    rectangle = list(map(int, input().split()))

    board = [[0] * 700 for _ in range(700)]
    A = rectangle[0:4]
    B = rectangle[4:]

    for j in range(A[1]+1, A[3]+2):
        for x in range(A[0], A[2]+1):
            board[700 - j][x] = 1

    for j in range(B[1]+1, B[3]+2):
        for x in range(B[0], B[2]+1):
            board[700-j][x] += 1

    res = [0, 0, 0, 0]



    # 맨처음에 검증 과정 check = 0 을 두고
    #  안쪽에 검증//// 만약에 안쪽에 있으면 check 를 1로 하고 다른거는 검증 안해도됨
    #  만약에 안쪽에 없으면 모서리 검증
    #  모서리 다음 선분 검증

    check  = 0
    # 안쪽에 있는지 없는지 검증
    # for ~~~
    # for ~~~
    # 있으면 break

    # 안쪽에 없으면 모서리 검증
    if check == 0:
        if board[700-A[1] - 1][A[0]] == 2 or board[700-A[1] - 1][A[2]] == 2 or board[700-A[3] - 1][A[0]] == 2 or board[700-A[3] - 1][A[2]] == 2:
            check = 2

    if check == 2:
        line = 0
        # 아래
        for i in range(A[0] + 1, A[2]):
            if board[700 - A[1] -1][i]== 2:
                line += 1

        # 오른쪽
        for i in range(A[1], A[3] - 1):
            if board[i][700-A[3] - 1] == 2:
                line += 1

        # 위쪽
        for i in range(A[0] + 1 , A[2]):
            if board[700-A[3] - 1][i] == 2:
                line += 1

        # 왼쪽
        for i in range(A[1], A[3] - 1):
            if board[i][A[0]] == 2:
                line += 1

    # for x in range(len(board)):
    #     print(board[x])



    print(check)
    print(line)


    # elif check == 1.5:
    #     print("선분 검증 차례")

    # 선분 검증
    # A 사각형 아랫줄
    # for i in range(A[0] + 1, A[2]):
    #     print(10 - A[1] - 1, i)
    #
    # A 사각형 오른쪽 줄


# 5 26 37 60 37 50 90 90


