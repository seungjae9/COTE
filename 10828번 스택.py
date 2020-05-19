# 10828번 스택
import sys
input=sys.stdin.readline


stack = ['0'] * 10000
idx = 0
for i in range(int(input())):
    order = input().split()
    if order[0] == "push":
        stack[idx] = order[1]
        idx += 1
    elif order[0] == "pop":
        if idx == 0:
            print(-1)
        else:
            idx -= 1
            print(stack[idx])
            stack[idx] = "0"
            if idx == -1:
                idx = 0
    elif order[0] == "top":
        if stack[idx-1] == "0":
            print(-1)
        else:
            print(stack[idx-1])
    elif order[0] == "size":
        if idx == 0:
            print(0)
        else:
            print(idx)
    elif order[0] == "empty":
        if idx == 0:
            print(1)
        else:
            print(0)
