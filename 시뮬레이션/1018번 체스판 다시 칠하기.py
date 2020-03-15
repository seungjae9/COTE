N, M = map(int, input().split())
board = [input() for _ in range(N)]
mini = 9999999
for i in range(0, N-7):
    for j in range(0, M-7):
        check = []
        for ii in range(i, i+8):
            temp = []
            for jj in range(j, j+8):
                temp.append(board[ii][jj])
            check.append(temp)
        W = 0
        B = 0
        for x in range(8):
            for y in range(8):
                if x % 2 == 0 and y % 2 == 0:
                    if check[x][y] != "W":
                        W += 1
                    if check[x][y] != "B":
                        B += 1
                if x % 2 == 0 and y % 2 != 0:
                    if check[x][y] != "B":
                        W += 1
                    if check[x][y] != "W":
                        B += 1
                if x % 2 != 0 and y % 2 == 0:
                    if check[x][y] != "B":
                        W += 1
                    if check[x][y] != "W":
                        B +=1
                if x % 2 != 0 and y % 2 != 0:
                    if check[x][y] != "W":
                        W +=1
                    if check[x][y] != "B":
                        B +=1
        if mini > min(W, B):
            mini = min(W, B)
print(mini)

