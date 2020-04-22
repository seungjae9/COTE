# # 16922번 로마 숫자 만들기

N = int(input())
origin = [1, 5, 10, 50]
roma = [1, 5, 10, 50]

cnt = 0
res = []
while cnt != N-1:
    for i in range(len(origin)):
        for j in range(4):
            if origin[i] + roma[j] not in res:
                res.append(origin[i] + roma[j])

    origin = res
    cnt += 1
    res = []
print(len(origin))
