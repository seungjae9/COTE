# 9012번 괄호


for i in range(int(input())):
    stack = 0
    for j in input():
        if j == "(":
            stack += 1
        else:
            stack -= 1
            if stack == -1:
                break

    if stack == 0:
        print("YES")
    else:
        print("NO")