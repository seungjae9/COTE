# 1292번 쉽게 푸는 문제

# A, B = map(int, input().split())
#
# number = []
# for i in range(45):
#     for j in range(i+1):
#         number.append(i+1)
#
# print(sum(number[A-1:B]))


A, B = map(int, input().split())
cnt = 1
number = []
for i in range(B):
    for j in range(cnt):
        number.append(cnt)
    cnt += 1

print(number)