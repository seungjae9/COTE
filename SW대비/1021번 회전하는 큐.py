# 1021번 회전하는 큐

N, M = map(int, input().split())
want = list(map(int, input().split()))
number = []
for i in range(N):
    number.append(i + 1)
ans = 0
for case in range(M):
    frontmin = 0
    backmin = 0
    if number[0] == want[case]:
        number = number[1::]
        frontlist = number
        backlist = number
    else:
        frontlist = number
        backlist = number

        while frontlist[0] != want[case]:
            front = frontlist[0]
            frontlist = frontlist[1::]
            frontlist.append(front)
            frontmin += 1
            if frontlist[0] == want[case]:
                frontlist = frontlist[1::]
                break

        while backlist[0] != want[case]:
            back = backlist[-1]
            backlist = backlist[0:len(backlist)-1]
            backlist.insert(0, back)
            backmin += 1
            if backlist[0] == want[case]:
                backlist = backlist[1::]
                break
    ans += min(frontmin, backmin)
    if frontmin < backmin:
        number = frontlist
    else:
        number = backlist

print(ans)


