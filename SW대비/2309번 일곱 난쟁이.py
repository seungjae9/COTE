# 2309번 일곱 난쟁이

# tall = []
# for i in range(9):
#     tall.append(int(input()))


def npr(n, k, N, s):
    if n == k:
        print(p)
    else:
        for i in range(s, N):
            if used[i] == 0:
                used[i] = 1
                p[n] = i+1
                npr(n+1, k, N, i)
                used[i] = 0

used = [0] * 9
p = [0] * 7
npr(0, 7, 9, 0)