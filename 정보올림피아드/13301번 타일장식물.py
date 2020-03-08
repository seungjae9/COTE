# 13301번 타일장식물

N = int(input())
number = [1, 1, 2] + [0] * (N -3)
if N >= 4:
    for i in range(3, N):
        number[i] = number[i-2] + number[i-1]
    print( (number[N-1] + number[N-2])*2 +(number[N-3] + number[N-2])*2)
elif N == 1:
    print(4)
elif N == 2:
    print(6)
elif N == 3:
    print(10)

