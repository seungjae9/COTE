# 2559번 수열

N, K = map(int, input().split())
temperature = list(map(int, input().split()))
increase = sum(temperature[0:K])
res = increase
for i in range(1, N-K+1):
    temp = increase - temperature[i-1] + temperature[i+K-1]
    if temp > res:
        res = temp
    increase = temp
print(res)