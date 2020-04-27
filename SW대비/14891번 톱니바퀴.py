# 14891번 톱니바퀴

condition = [list(map(int, input())) for _ in range(4)]
K = int(input())
turn = [list(map(int, input().split())) for _ in range(K)]


direction1 = [1, -1, 1, -1]
direction2 = [-1, 1, -1, 1]
for i in range(K):
    change = [0,0,0,0]
    if turn[i][0] == 1:
        check = [1, 0, 0, 0]
        if condition[0][2] == 0 and condition[1][6] == 1 or condition[0][2] == 1 and condition[1][6] == 0:
            check[1] = 1
        if condition[1][2] == 0 and condition[2][6] == 1 and check[1] == 1 or condition[1][2] == 1 and condition[2][6] == 0 and check[1] == 1:
            check[2] = 1
        if condition[2][2] == 0 and condition[3][6] == 1 and check[2] == 1 or condition[2][2] == 1 and condition[3][6] == 0 and check[2] == 1:
            check[3] = 1
    elif turn[i][0] == 2:
        check = [0, 1, 0, 0]
        if condition[1][6] == 0 and condition[0][2] == 1 or condition[1][6] == 1 and condition[0][2] == 0:
            check[0] = 1
        if condition[1][2] == 0 and condition[2][6] == 1 or condition[1][2] == 1 and condition[2][6] == 0:
            check[2] = 1
        if condition[2][2] == 0 and condition[3][6] == 1 and check[2] == 1 or condition[2][2] == 1 and condition[3][6] == 0 and check[2] == 1:
            check[3] = 1
    elif turn[i][0] == 3:
        check = [0, 0, 1, 0]
        if condition[2][2] == 0 and condition[3][6] == 1 or condition[2][2] == 1 and condition[3][6] == 0:
            check[3] = 1
        if condition[2][6] == 0 and condition[1][2] == 1 or condition[2][6] == 1 and condition[1][2] == 0:
            check[1] = 1
        if condition[1][6] == 0 and condition[0][2] == 1 and check[1] == 1 or condition[1][6] == 1 and condition[0][2] == 0 and check[1] == 1:
            check[0] = 1
    elif turn[i][0] == 4:
        check = [0, 0, 0, 1]
        if condition[3][6] == 0 and condition[2][2] == 1 or condition[3][6] == 1 and condition[2][2] == 0:
            check[2] = 1
        if condition[2][6] == 0 and condition[1][2] == 1  and check[2] == 1 or condition[2][6] == 1 and condition[1][2] == 0 and check[2] == 1:
            check[1] = 1
        if condition[1][6] == 0 and condition[0][2] == 1 and check[1] == 1 or condition[1][6] == 1 and condition[0][2] == 0 and check[1] == 1:
            check[0] = 1

    if turn[i][0] == 1 and turn[i][1] == 1 or turn[i][0] == 2 and turn[i][1] == -1 or turn[i][0] == 3 and turn[i][1] == 1 or turn[i][0] == 4 and turn[i][1] == -1:
        for j in range(4):
            if check[j] == 1:
                change[j] = direction1[j]
    elif turn[i][0] == 1 and turn[i][1] == -1 or turn[i][0] == 2 and turn[i][1] == 1 or turn[i][0] == 3 and turn[i][1] == -1 or turn[i][0] == 4 and turn[i][1] == 1:
        for j in range(4):
            if check[j] == 1:
                change[j] = direction2[j]


    for x in range(4):
        if change[x] == 1:
            back = condition[x][-1]
            condition[x] = condition[x][0:7]
            condition[x].insert(0, back)
        elif change[x] == -1:
            front = condition[x][0]
            condition[x] = condition[x][1:8]
            condition[x].append(front)

ans = 0
for i in range(4):
    if condition[i][0] == 1:
        ans += 2**i
print(ans)