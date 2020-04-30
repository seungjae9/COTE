# 3190번 뱀

N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
for i in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

L = int(input())
direction = [list(input().split()) for _ in range(L)]

x = 0
y = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(len(board)):
    print(board[i])
compass = 1   # 1은 동쪽, 2는 남쪽 3은 서쪽 4는 북쪽

for case in range(L):
    if direction[case][1] == "D":
        compass = (compass + 1) % 4
    elif direction[case][1] == "L":
        compass = (compass + 3) % 4




