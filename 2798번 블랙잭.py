# 2798번 블랙잭
#
# N, M = map(int, input().split())
# card = list(map(int, input().split()))
# total = len(card)
#
# maxsum = 0
# for i in range(total):
#     for j in range(i+1, total):
#         for x in range(j+1, total):
#             temp = 0
#             temp += card[i] + card[j] + card[x]
#             if maxsum <= temp <= M:
#                 maxsum = temp
#
# print(maxsum)


import itertools
N, M = map(int, input().split())
card = list(map(int, input().split()))
maxsum = 0
for i in itertools.combinations(card, 3):
    if maxsum <= sum(i) <= M:
        maxsum = sum(i)
print(maxsum)


