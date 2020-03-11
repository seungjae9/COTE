# 1526번 가장 큰 금민수

N = int(input())
a = 0
x = 0
number = ["4", "7"]
while True:
    for i in range(x, len(number)):

        if int(number[-1]) >= N:
            a = 1
            break
        number.append(number[i] + "4")

        if int(number[-1]) >= N:
            a = 1
            break
        number.append(number[i] + "7")

        x += 1
    if a == 1:
        break

if N == int(number[-1]):
    print(N)
else:
    print(number[-2])
