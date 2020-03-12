# 3985번 롤케이크

L = [1] * int(input())
want = []
for i in range(int(input())):
    want.append(list(map(int, input().split())))
wish = []
real = []
for i in range(len(want)):
    real.append(sum(L[want[i][0]-1:want[i][1]]))
    for j in range(want[i][0]-1, want[i][1]):
        L[j] = 0
for i in range(len(want)):
    wish.append(want[i][1] - want[i][0] +1)
print(wish.index(max(wish))+1)
print(real.index(max(real))+1)

