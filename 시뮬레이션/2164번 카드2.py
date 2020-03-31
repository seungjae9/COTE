#2164번 카드2

number = []
N = int(input())
for i in range(N):
    number.append(i+1)

res = []

front = 0

for i in range(N-1):
    res.append(number[front])
    front += 1
    number[front], number[-1] = number[-1], number[front]
    print(number)

res.append(number[0])
res = " ".join(map(str, res))

print(number[-1])


#
# 1
# 2
# 3
# 4
#
# #
# 1 2 3 4
# 1 3 4 2
# 1 3 2 4
# 1 2 3 4
# 1 3 4 2