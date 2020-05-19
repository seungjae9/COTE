# 10773번 제로
import sys
input = sys.stdin.readline

money = []
for i in range(int(input())):
    number = int(input())
    if number == 0:
        money.pop()
    else:
        money.append(number)

print(sum(money))