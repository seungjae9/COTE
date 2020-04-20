# 2422번 한윤정이 이탈리아에 가서 아이스크림을 사먹는데



# N, M = map(int, input().split())
# x = [list(map(int, input().split())) for _ in range(M)]
#
# number = []
# for i in range(N):
#     number.append(i+1)
#
#
# case = [[]]
#
# for i in range(N-2):
#     for j in range(i+1, N-1):
#         for x in range(j+1, N):
#             # print(number[i], number[j], number[x])
#


n,m = map(int,input().split())
a = [[False]*n for _ in range(n)]
for _ in range(m):
    u,v = map(int,input().split())
    a[u-1][v-1] = a[v-1][u-1] = True
ans = 0
# print(a)
for i in range(len(a)):
    print(a[i])
for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if a[i][j] or a[j][k] or a[k][i]:
                # print(a[i][j])
                # print(a[j][k])
                # print(a[k][i])
                # print()
                continue
            print(a[i][j])
            print(a[j][k])
            print(a[k][i])
            print()
            ans += 1
print(ans)