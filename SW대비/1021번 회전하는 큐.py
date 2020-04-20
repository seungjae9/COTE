# 1021번 회전하는 큐

N, M = map(int, input().split())
want = list(map(int, input().split()))


# 앞으로 뒤로 해서 최솟값을 저장하면 될듯(부르트 포스 방식)

number = []
for i in range(N):
    number.append(i+1)

for i in range(M):

    front = number[0]
    back = number[-1]

    frontnumber = number.copy()
    backnumber = number.copy()

    if front == want[i]:
        del number[0]

    elif front != want[i]:
        backcheck = 0
        frontcheck = 0

        while frontnumber[0] != want[i]:
            for j in range(len(frontnumber)):
                if frontnumber[j] == 1:
                    frontnumber[j] = N
                else:
                    frontnumber[j] -= 1
            backcheck += 1
            frontnumber[0] = back
            back = frontnumber[-1]
            if frontnumber[0] == want[i]:
                break
            print(frontnumber)

        #
        # while backnumber[0] != want[i]:
        #     for j in range(len(backnumber)):
        #         if backnumber[j] >= N:
        #             backnumber[j] = 1
        #         else:
        #             backnumber[j] += 1
        #     frontcheck += 1
        #     backnumber[-1] = front
        #     front = backnumber[0]
        #     if backnumber[0] == want[i]:
        #         break
        #
        #
        # if frontcheck < backcheck:
        #     number = frontnumber.copy()
        #
        # else:
        #     number = backnumber.copy()

        del number[0]

        # print(frontcheck, backcheck)



# 1 2 3 4 5 6 7 8 9 10
# 10 1 2 3 4 5 6 7 8 9
# 9 10 1 2 3 4 5 6 7 8

# 1 2 3 4 5 6 7 8 9
# 2 3 4 5 6 7 8 9 10

# 2 3 4 5 6 7 8 9 1
#

# 1 2 3 4 5 6 7 8 9
# 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8
# 9 2 3 4 5 6 7 8


# 6 3 2 7 9 8 4 10 5
