# 1551번 수열의 변화

N, K = map(int, input().split())
number = input()
number = number.split(',')

res = []
for i in range(K):
    res.append(number)