# 7562번 나이트의 이동

di = [1, 1, 2, 2, -1, -1, -2, -2]
dj = [2, -2, 1, -1, 2, -2, 1, -1]
def bfs(x, y, c, d):
    q = []
    q.append([x,y])
    while q:
        a, b = q.pop(0)
        if a == c and b == d:
            print(board[a][b])
            return
        for i in range(8):
            ni = a + di[i]
            nj = b + dj[i]
            if 0 <= ni < l and 0 <= nj < l and board[ni][nj] == 0:
                board[ni][nj] = board[a][b] + 1
                q.append([ni, nj])
for case in range(int(input())):
    l = int(input())
    board = [[0] * l for _ in range(l)]
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    bfs(a, b, c, d)
