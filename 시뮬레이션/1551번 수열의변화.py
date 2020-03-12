# 1551번 수열의 변화


N, K = map(int, input().split())
number = list(map(int, input().split(',')))

if K > 0:
    for i in range(K):
        res = []
        for j in range(len(number)-1):
            res.append(number[j+1] - number[j])
        number = res
    res = ",".join(map(str, res))
    print(res)

elif K == 0:
    number = ",".join(map(str, number))
    print(number)