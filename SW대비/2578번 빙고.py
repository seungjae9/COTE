# 2578번 빙고
bingo = [list(map(int, input().split())) for _ in range(5)]
MC = [list(map(int, input().split())) for _ in range(5)]

res = 0
stop = 0

for i in range(5):
    for j in range(5):
        sign = MC[i][j]
        res += 1
        breakpoint = 0
        for x in range(5):
            for t in range(5):
                if bingo[x][t] == sign:
                    bingo[x][t] = "*"
                    breakpoint = 1
                    break
            if breakpoint == 1:
                break
        check = 0
        for row in range(5):
            if bingo[row].count("*") >= 5:
                check +=1
        check2 = 0
        for col in range(5):
            temp = 0
            for fix in range(5):
                if bingo[fix][col] == "*":
                    temp += 1
            if temp == 5:
                check2 +=1
        check3 = 0
        check4 = 0
        temp2 = 0
        temp3 = 0
        for diagonal in range(5):
            if bingo[diagonal][diagonal] == "*":
                temp2 +=1
            if bingo[diagonal][4 - diagonal] == "*":
                temp3 += 1
        if temp2 == 5:
            check3 = 1
        if temp3 == 5:
            check4 = 1

        if check + check2 + check3 + check4 >= 3:
            stop = 1
            print(res)
            break
    if stop == 1:
        break

