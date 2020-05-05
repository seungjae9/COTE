# #
#  2627번 단지번호붙이기
# # BFS

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def search(x, y, N):
    q = []
    q.append([x, y])
    apartment[x][y] = 0
    site = 1
    while q:

        a, b = q.pop(0)
        for i in range(4):
            ni = a + di[i]
            nj = b + dj[i]
            if 0 <= ni <= N - 1 and 0 <=  nj <= N -1 and apartment[ni][nj] == 1:
                q.append([ni, nj])
                apartment[ni][nj] = 0
                site += 1
    return site

N = int(input())
apartment = [list(map(int, input())) for _ in range(N)]

cnt = 0
checker = []
for i in range(N):
    for j in range(N):
        if apartment[i][j] == 1:
            cnt += 1
            checker.append(search(i, j, N))

checker.sort()
print(cnt)
for i in range(cnt):
    print(checker[i])
