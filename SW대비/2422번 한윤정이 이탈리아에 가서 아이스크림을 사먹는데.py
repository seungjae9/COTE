# 2422번 한윤정이 이탈리아에 가서 아이스크림을 사먹는데

N, M = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(M)]

number = [[0] * N for _ in range(N)]

# 방문 개념
for i in range(M):
    number[x[i][0] - 1][x[i][1] - 1], number[x[i][1] - 1][x[i][0] - 1] = "x", "x"

res = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for x in range(j+1, N):
            # 컨티뉴는 pass와 다르게 계속 해서 다음번 for문 loop를 호출
            if number[i][j] or number[j][x] or number[x][i] == "x":
                continue
            res += 1
print(res)

