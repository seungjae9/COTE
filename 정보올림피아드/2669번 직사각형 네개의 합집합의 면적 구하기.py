# 2669번 직사각형 네개의 합집합의 면적 구하기

board = []
for i in range(100):
    temp = [0] * 100
    board.append(temp)

# 판때가리 만들떄 원래 이렇게 했었는데 까먹음
# => board = [[0] * 100 for _ in range(100)]


coordinate = []
for coord in range(4):
    coordinate.append(list(map(int, input().split())))
for i in range(4):
    for y in range(coordinate[i][3] - coordinate[i][1]):
        for x in range(coordinate[i][2] - coordinate[i][0]):
            board[y + coordinate[i][1]][x + coordinate[i][0]] = 1
#=> range범위 정할때 이렇게 받았는데 이것도 까먹음
# for coord in range(4):
#     coordinate = list(map(int, input().split()))
#     for i in range(coordinate[1], coordinate[3]):
#         for j in range(coordinate[0], coordinate[2]):
#             board[i][j] = 1

res = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1:
            res +=1

print(res)