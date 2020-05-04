# 11723번 집합

import sys
n = int(sys.stdin.readline())
S = ["0"] * 21
for i in range(n):
    order = sys.stdin.readline().split()
    if order[0] == "add" and S[int(order[1])] == "0":
        S[int(order[1])] = "1"
    elif order[0] == "remove" and S[int(order[1])] == "1":
        S[int(order[1])] = "0"
    elif order[0] == "check":
        if S[int(order[1])] == "1":
            print(1)
        else:
            print(0)
    elif order[0] == "toggle":
        if S[int(order[1])] == "1":
            S[int(order[1])] = "0"
        else:
            S[int(order[1])] = "1"
    elif order[0] == "all":
        S = ["1"] * 21
    elif order[0] == "empty":
        S = ["0"] * 21
