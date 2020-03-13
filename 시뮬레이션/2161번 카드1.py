number = []
N = int(input())
for i in range(N):
    number.append(i+1)


res = []
for i in range(N-1):
    res.append(number[0])
    del number[0]
    number.append(number[0])
    del number[0]
res.append(number[0])
res = " ".join(map(str, res))
print(res)