# 1592번 영식이와 친구들

N, M, L = map(int, input().split())
check = [1] + [0] * (N-1)
ball = 0
while M not in check:
    if check[ball] % 2 != 0:
        ball += L
        if ball >= N:
            ball -= N
        check[ball] += 1
    else:
        ball -= L
        if ball < -N:
            ball += N
        check[ball] += 1
print(sum(check)-1)

