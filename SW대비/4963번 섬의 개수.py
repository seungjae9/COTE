# 4963번 섬의 개수

di = [-1, -1, -1, 0, 1, 1, 1, 0]
dj = [-1, 0, 1, 1, 1, 0, -1, -1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    else:
        island = [list(map(int, input().split())) for _ in range(h)]
        def bfs(x, y, w, h):
            q = []
            q.append([x, y])
            while q:
                a, b = q.pop(0)
                for t in range(8):
                    ni = a + di[t]
                    nj = b + dj[t]
                    if 0 <= ni < h and 0 <= nj < w and island[ni][nj] == 1:
                        island[ni][nj] = 0
                        q.append([ni, nj])
        cnt = 0
        for i in range(h):
            for j in range(w):
                if island[i][j] == 1:
                    cnt += 1
                    bfs(i, j, w, h)
        print(cnt)