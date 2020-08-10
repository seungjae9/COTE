# 큰수의 법칙

N, M, K = map(int, input().split())
number = list(map(int, input().split()))


number.sort(reverse=True)
info = []
check = 0
for i in number:
    if len(info) < 3:
        if i not in info:
            info.append(i)

        elif i in info:
            check = 1
    else:
        break
ans = 0
x = 0
if check == 0:
    for i in range(M):
        if x != K:
            x += 1
            ans += info[0]
        else:
            ans += info[1]
            x = 0
else:
    ans = info[0] * M



print(ans)