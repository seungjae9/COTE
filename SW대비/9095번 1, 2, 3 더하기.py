# 9095번 1, 2, 3 더하기

for i in range(int(input())):
    plus = [1, 2, 4, 7]
    n = int(input())
    for j in range(4, n):
        plus.append(plus[j-3] + plus[j-2] + plus[j-1])
    print(plus[n-1])
