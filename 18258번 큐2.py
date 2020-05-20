# 18258번 큐 2

import sys
input = sys.stdin.readline

queue = ["0"] * 2000000
idx = 0
ahead = 0
val = 0
for i in range(int(input())):
    order = input().split()
    if order[0] == "push":
        queue[idx] = order[1]
        idx += 1
        val += 1
    elif order[0] == "pop":
        if queue[ahead] != "0":
            print(queue[ahead])
            queue[ahead] = "0"
            ahead += 1
            val -= 1
        else:
            print(-1)
    elif order[0] == "size":
        print(val)
    elif order[0] == "front":
        if queue[ahead] != "0":
            print(queue[ahead])
        else:
            print(-1)

    elif order[0] == "back":
        if queue[idx-1] != "0":
            print(queue[idx-1])
        else:
            print(-1)
    elif order[0] == "empty":
        if val == 0:
            print(1)
        else:
            print(0)



