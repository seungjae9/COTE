# 17614번 369

N = int(input())
res = 0
for i in range(N):
    i = str(i+1)
    res += i.count('3') + i.count('6') + i.count('9')
print(res)


# 그때 그때 처리하는게 느린가보다.
# res = 0
# for i in range(int(input())):
#     res += str(i+1).count('3') + str(i+1).count('6') + str(i+1).count('9')
# print(res)
#
