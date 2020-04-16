# 14697번 방 배정하기

A, B, C, N = map(int, input().split())

res = 0
for i in range(N // A + 1):
    for j in range(N // B + 1):
        for x in range(N // C + 1):
            if A * i + B * j + C * x == N:
               res = 1
print(res)