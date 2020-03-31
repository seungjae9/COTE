# 2979번 트럭 주차
A, B, C = map(int, input().split())
timemax = 0
time = []
for i in range(3):
    a = list(map(int, input().split()))
    time.append(a)
    if timemax < max(a):
        timemax = max(a)
truck = [0] * timemax

for i in range(3):
    for j in range(time[i][0], time[i][1]):
        truck[j-1] += 1
res = 0
for i in truck:
    if i == 1:
        res += i*A
    elif i == 2:
        res += 2*B
    elif i == 3:
        res += 3*C
print(res)