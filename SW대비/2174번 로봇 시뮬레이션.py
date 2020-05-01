# # 2174번 로봇 시뮬레이션
#
# A, B = map(int, input().split())
# N, M = map(int, input().split())
# location = [list(input().split()) for _ in range(N)]
# order = [list(input().split()) for _ in range(M)]
#
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# # 동서남북, 1234
# board = [[0] * (A+1) for _ in range(B+1)]
# direction = []
# for i in range(N):
#     board[int(location[i][1])-1][int(location[i][0])-1] = i + 1
#     if location[i][2] == "N":
#         direction.append(1)
#     elif location[i][2] == "E":
#         direction.append(2)
#     elif location[i][2] == "S":
#         direction.append(3)
#     else:
#         direction.append(4)
# ans = []
#
# for i in range(len(board)):
#     print(board[i])
# print()
# def left(direc, many):
#     for i in range(many):
#         direc -= 1
#         if direc == 0:
#             direc = 4
#
# def right(direc, many):
#     for i in range(many):
#         direc += 1
#         if direc == 5:
#             direc = 1
#
# res = []
# def east(j, i, many, search):
#     print(many)
#     for go in range(many):
#         if j + dy[1] <= A:
#             if board[i][j + dy[1]] != 0:
#                 res.append("Robot {} crashes into robot {}".format(search, board[i][j+1]))
#                 break
#             else:
#                 board[i][j], board[i][j+1] = 0, search
#                 j += 1
#         else:
#             res.append("Robot {} crashes into the wall".format(search))
#             break
#
# def west(j, i, many, search):
#     for go in range(many):
#         if j + dy[3] >= 0:
#             if board[i][j + dy[3]] != 0:
#                 res.append("Robot {} crashes into robot {}".format(search, board[i][j+1]))
#                 break
#             else:
#                 board[i][j], board[i][j-1] = 0, search
#                 j -= 1
#         else:
#             res.append("Robot {} crashes into the wall".format(search))
#             break
#
# def north(j, i, many, search):
#     for go in range(many):
#         if i + dy[0] >= 0:
#             if board[i + dy[0]][j] != 0:
#                 res.append("Robot {} crashes into robot {}".format(search, board[i-1][j]))
#                 break
#             else:
#                 board[i][j], board[i-1][j] = 0, search
#                 i -= 1
#         else:
#             res.append("Robot {} crashes into the wall".format(search))
#             break
#
# def south(j, i, many, search):
#     for go in range(many):
#         if i + dy[2] >= 0:
#             if board[i + dy[2]][j] != 0:
#                 res.append("Robot {} crashes into robot {}".format(search, board[i+1][j]))
#                 break
#             else:
#                 board[i][j], board[i+1][j] = 0, search
#                 i += 1
#         else:
#             res.append("Robot {} crashes into the wall".format(search))
#             break
#
# for case in range(M):
#     if len(res) > 0:
#         break
#     else:
#         search = int(order[case][0])
#         if order[case][1] == "L":
#             left(direction[search-1], int(order[case][2]))
#         elif order[case][1] == "R":
#             right(direction[search-1], int(order[case][2]))
#         elif order[case][1] == "F":
#             if direction[search-1] == 1:
#                 north(int(location[search-1][1]) - 1, int(location[search-1][0]) - 1, int(order[case][2]), search)
#             elif direction[search - 1] == 2:
#                 east(int(location[search-1][1]) - 1, int(location[search-1][0]) - 1, int(order[case][2]), search)
#             elif direction[search - 1] == 4:
#                 west(int(location[search-1][1]) -1, int(location[search-1][0]) -1, int(order[case][2]), search)
#             else:
#                 south(int(location[search-1][1]) -1, int(location[search-1][0]) -1, int(order[case][2]), search)
#
#
# for i in range(len(board)):
#     print(board[i])
#
# print(res)
#
#
