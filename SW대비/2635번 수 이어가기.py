# 2635번 수 이어가기

N = int(input())
initial = N

ans = []
for i in range(initial):
    res = [N]
    res.append(initial)
    temp = initial
    temp2 = N
    while temp2 - temp >= 0:

        res.append(res[-2] - res[-1])

        temp = res[-1]
        temp2 = res[-2]
    initial -= 1
    if len(ans) <= len(res):
        ans = res

print(len(ans))
print(" ".join(map(str, ans)))
