# 5397번 키로거

for t in range(int(input())):

    a = ["-"] * 1000000
    idx = 0
    case = input()

    maxidx = 0
    for i in case:
        if i == "<":
            idx -= 1
            if idx == -1:
                idx = 0
        elif i == ">":
            idx += 1
            if idx > maxidx:
                idx = maxidx
        elif i == "-":
            a[idx-1] = "-"
            idx -= 1
            maxidx -= 1
            if idx == -1:
                idx = 0
                maxidx = 0

        else:
            a[idx] = i
            idx += 1
            print(idx)
            maxidx += 1

    for xxx in a:
        if xxx != "-":
            print(xxx)
    # print(a)