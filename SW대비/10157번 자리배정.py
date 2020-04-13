# 10157번 자리배정

C, R = map(int, input().split())
K = int(input())

board = [[0] * C for _ in range(R)]


check = 1
# 몇번 돌지
up = R
right = C - 1
down = R - 1
left = C - 2

# 처음 찍히는 곳
x = R - 1
y = 0


while check - 1 != R * C:

    for i in range(up):
        board[x][y] = check
        x -= 1
        check +=1

    up -=2
    y += 1
    x += 1

    if check - 1 == R * C:
        break


    for i in range(right):
        board[x][y] = check
        y +=1
        check +=1

    right -= 2
    y -= 1
    x += 1

    if check - 1 == R * C:
        break

    for i in range(down):
        board[x][y] = check
        x += 1
        check +=1

    down -= 2
    x -= 1
    y -= 1

    if check - 1 == R * C:
        break

    for i in range(left):
        board[x][y] = check
        y -= 1
        check += 1
    left -=2
    y += 1
    x -= 1

    if check - 1 == R * C:
        break


if R * C < K:
    print(0)
else:
    for i in range(R):
        for j in range(C):
            if board[i][j] == K:
                print(j+1, R - i)
