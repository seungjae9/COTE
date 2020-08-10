# 11047번 동전 0 

N, K = map(int, input().split())
A = []
for i in range(N):
    A.append(int(input()))
A.sort(reverse=True)
ans = 0
for i in A:
    if K ==0:
        break
    ans += K // i
    K %= i
print(ans)

