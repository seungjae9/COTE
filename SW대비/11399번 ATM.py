# 11399번 ATM

N = int(input())
temp = 0
res = 0
for i in sorted(list(map(int, input().split()))):
    temp += i
    res += temp
print(res)