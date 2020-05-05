# 1012번 유기농 배추

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for case in range(int(input())):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]

    for i in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1


    def bfs(i, j):
        q = []
        q.append([i, j])
        while q:
            a, b = q.pop(0)
            for x in range(4):
                ni = a + di[x]
                nj = b + dj[x]
                if 0 <= ni < N and 0 <= nj < M and field[ni][nj] == 1:
                    field[ni][nj] = 0
                    q.append([ni, nj])


    cnt = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                cnt += 1
                bfs(i, j)

    print(cnt)