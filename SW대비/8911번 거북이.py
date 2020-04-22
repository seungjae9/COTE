


for case in range(int(input())):

    control = input()

    board = [[0] * 60 for _ in range(60)]

    board[30][30] = "0" #가운데 원점임


    x, y = 30, 30


    for i in control:
        if i == "F":
            board[x][y] = "Y"
            turtle = -1
            x += turtle
        elif i == "L":
            turtle = -1

    for i in range(60):
        print(board[i])
