# # 14503번 로봇 청소기

N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


def up(r, c, d):
    d = 3
    if 0 <= c - 1:
        if board[r][c-1] == 0:
            c -= 1

    return r, c, d

def left(r, c, d):
    d = 2
    if r + 1 < N:
        if board[r+1][c] == 0:
            r += 1
    return r, c, d

def down(r, c, d):
    d = 1
    if c + 1 < M:
        if board[r][c+1] == 0:
            c += 1

    return r, c, d

def right(r, c, d):
    d = 0
    if 0 <=  r - 1:
        if board[r-1][c] == 0:
            r -= 1

    return r, c, d


cnt = 0

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
point = 0

for i in range(20):
    if board[r][c] == 0:
        cnt += 1
        board[r][c] = "X"

    temp = 0
    for i in range(4):
        ni = r + di[i]
        nj = c + dj[i]
        if 0 <= ni < N and 0 <= nj < M and board[ni][nj] == 1 or 0 <= ni < N and 0 <= nj < M and board[ni][nj] == "X":
            temp += 1

    print(temp)
    if temp == 4:
        if d == 0:
            if board[r+1][c] != 1:
                r +=1
            elif board[r+1][c] == 1:
                point = 1
        elif d == 1:
            if board[r][c-1] != 1:
                c -= 1
            elif board[r + 1][c] == 1:
                point = 1
        elif d == 2:
            if board[r-1][c] != 1:
                r -= 1
            elif board[r + 1][c] == 1:
                point = 1
        elif d == 3:
            if board[r][c+1] != 1:
                c += 1
            elif board[r + 1][c] == 1:
                point = 1

    print(point)
    if point == 1:
        break

    temp = 0

    if d == 0:
        r, c, d = up(r, c, d)
    elif d == 3:
        r, c, d = left(r, c, d)
    elif d == 2:
        r, c, d = down(r, c, d)
    elif d == 1:
        r, c, d = right(r, c, d)

    print(r, c, d)


print(cnt)




















# N, M = map(int, input().split())
# r, c, d = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
# r -= 1
# c -= 1
# di = [-1, 0, 1, 0]
# dj = [0, 1, 0, -1]
# clean = 0
#
# def north(x, y, direction):
#     if board[x][y-1] == 0:
#         y -= 1
#         direction = 3
#     else:
#         direction = 3
#
#     return x, y, direction
#
# def east(x, y, direction):
#     if board[x-1][y] == 0:
#         x -= 1
#         direction = 0
#     else:
#         direction = 0
#
#     return x, y, direction
#
# def south(x, y, direction):
#     if board[x][y+1] == 0:
#         y += 1
#         direction = 1
#     else:
#         direction = 1
#     return x, y, direction
#
# def west(x, y, direction):
#     if board[x+1][y] == 0:
#         x += 1
#         direction = 2
#     else:
#         direction = 2
#
#     return x, y, direction
# while True:
#     if board[r][c] == 0:
#         board[r][c] = 2
#         clean += 1
#     checkpoint = 0
#     for i in range(4):
#         ni = r + di[i]
#         nj = c + dj[i]
#         if ni == 1 or nj == 1:
#             checkpoint += 1
#     if checkpoint == 4:
#         if d == 0:
#             if board[r-1][c] == 1:
#                 break
#             else:
#                 r -= 1
#         elif d == 1:
#             if board[r][c+1] == 1:
#                 break
#             else:
#                 c += 1
#         elif d == 2:
#             if board[r+1][c] == 1:
#                 break
#             else:
#                 r += 1
#         elif d == 3:
#             if board[r][c-1] == 1:
#                 break
#             else:
#                 c -= 1
#     if d == 0:
#         r, c, d = north(r, c, d)
#
#     elif d == 1:
#         r, c, d = east(r, c, d)
#
#     elif d == 2:
#         r, c, d = south(r, c, d)
#
#     elif d == 3:
#         r, c, d, = west(r, c, d)
#
#     print(clean)
#     for x in range(len(board)):
#         print(board[x])
#     print()
#
#
# print(clean)
# print(r, c, d)
