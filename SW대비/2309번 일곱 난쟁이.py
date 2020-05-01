# 2309번 일곱 난쟁이

# tall = []
# for i in range(9):
#     tall.append(int(input()))
#
# point = 0
# res =[]
# for i in range(3):
#     for j in range(i+1, 4, 1):
#         for x in range(j+1, 5, 1):
#             for t in range(x+1, 6, 1):
#                 for c in range(t+1, 7, 1):
#                     for q in range(c+1, 8, 1):
#                         for v in range(q+1, 9, 1):
#                             if tall[i] + tall[j] + tall[x] + tall[t] + tall[c] + tall[q] + tall[v] == 100:
#                                 res.append(tall[i])
#                                 res.append(tall[j])
#                                 res.append(tall[x])
#                                 res.append(tall[t])
#                                 res.append(tall[c])
#                                 res.append(tall[q])
#                                 res.append(tall[v])
#                                 point = 1
#                                 break
#                         if point == 1:
#                             break
#                     if point == 1:
#                         break
#                 if point == 1:
#                     break
#             if point == 1:
#                 break
#         if point == 1:
#             break
#     if point == 1:
#         break
#
#
# for i in sorted(res):
#     print(i)


tall = []
for i in range(9):
    tall.append(int(input()))

pls = 0
for c in tall:
    pls += c

result =[]
for x in range(9):
    for j in range(x+1, 9):
        if pls - tall[x] - tall[j] == 100:
            result.append(tall[x])
            result.append(tall[j])
            break
tall.remove(result[0])
tall.remove(result[1])
tall.sort()

for c in range(7):
    print(tall[c])