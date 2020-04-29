# for case in range(int(input())):
#     control = input()
#     board = [[0] * 10 for _ in range(10)]
#     turtle_x = 5
#     turtle_y = 5
#
#     initial = 0
#
#     for i in range(len(control)):
#         if control[i] == "L" and initial == 0 or control[i] == "L" and initial == -1 or control[i] == "R" and initial == 1 or control[i] == "R" and initial == 2:
#             turtle_x += 1
#             turtle_y -= 1
#             initial -= 1
#         elif control[i] == "L" and initial == -2 or control[i] == "L" and initial == --3 or control[i] == "R" and initial == 0 or control[i] == "R" and initial == 3:
#             turtle_x -= 1
#             turtle_y += 1
#             initial += 1
#
#         if initial == 4 or initial == -4:
#             initial = 0
#
#         if control[i] == "F" and initial == 0:
#             board[turtle_x][turtle_y] = 1
#             turtle_x -= 1
#         elif control[i] == "F" and initial == -1 or control[i] == "F" and initial == 3:
#             board[turtle_x][turtle_y] = 1
#             turtle_y -= 1
#         elif control[i] == "F" and initial == -2 or control[i] == "F" and initial == 2:
#             board[turtle_x][turtle_y] = 1
#             turtle_x += 1
#         elif control[i] == "F" and initial == -3 or control[i] == "F" and initial == 1:
#             board[turtle_x][turtle_y] = 1
#             turtle_y += 1
#
#         elif control[i] == "B" and initial == 0:
#             board[turtle_x][turtle_y] = 1
#             turtle_x += 1
#         elif control[i] == "B" and initial == -1 or control[i] == "B" and initial == 3:
#             board[turtle_x][turtle_y] = 1
#             turtle_y += 1
#         elif control[i] == "B" and initial == -2 or control[i] == "B" and initial == 2:
#             board[turtle_x][turtle_y] = 1
#             turtle_x -= 1
#         elif control[i] == "B" and initial == -3 or control[i] == "B" and initial == 1:
#             board[turtle_x][turtle_y] = 1
#             turtle_y -= 1
#
#     for i in range(len(board)):
#         print(board[i])
#     print()



# def up(X, Y):
#     board[X][Y] = 1
#     # Y -= 1
#     return X, Y
#
# def left(X, Y):
#     # X -= 1
#     board[X][Y] = 1
#     return X, Y
#
#
# for case in range(int(input())):
#     control = input()
#     board = [[0] * 20 for _ in range(20)]
#     turtle_x = 10
#     turtle_y = 10
#
#     initial = 0
#
#     for i in range(len(control)):
#         if control[i] == "L":
#             initial = 3
#         if control[i] == "F" and initial == 0:
#             turtle_x -= 1
#             turtle_x, turtle_y = up(turtle_x, turtle_y)
#         if control[i] == "F" and initial == 3:
#             turtle_y -= 1
#             turtle_x, turtle_y = left(turtle_x, turtle_y)
#
#
#     for i in range(len(board)):
#         print(board[i])







# for case in range(int(input())):
#
#     control = input()
#
#     board = [[0] * 60 for _ in range(60)]
#
#     board[30][30] = "0" #가운데 원점임
#
#
#     x, y = 30, 30
#
#
#     for i in control:
#         if i == "F":
#             board[x][y] = "Y"
#             turtle = -1
#             x += turtle
#         elif i == "L":
#             turtle = -1
#
#     for i in range(60):
#         print(board[i])
