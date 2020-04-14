# 2605번 줄 세우기

N = int(input())
row = list(map(int, input().split()))

res = [1]
for i in range(1, len(row)):
    if row[i] == 0:
        res.insert(0, i+1)
    else:
        res.insert(row[i], i+1)
res.reverse()
print(" ".join(map(str, res)))
