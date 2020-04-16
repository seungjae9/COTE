# 1244번 스위치 켜고 끄기

N = int(input())
switch = list(map(int, input().split()))
student = int(input())
number = [list(map(int, input().split())) for _ in range(student)]


for i in range(student):
    if number[i][0] == 1:
        for j in range(N):
            if (j + 1) % number[i][1] == 0:
                if switch[j] == 1:
                    switch[j] = 0
                else:
                    switch[j] = 1
    elif number[i][0] == 2:
        for j in range(1, N):
            if number[i][1] - 1  - j >= 0 and number[i][1] - 1 + j <= N-1:
                if switch[number[i][1] - 1- j] == switch[number[i][1] - 1 + j]:
                    if switch[number[i][1] - 1 - j] == 0:
                        switch[number[i][1] - 1 - j] = 1
                        switch[number[i][1] - 1 + j] = 1
                    else:
                        switch[number[i][1] - 1 - j] = 0
                        switch[number[i][1]  -1 + j] = 0
                else:
                    break
        if switch[number[i][1] - 1] == 0:
            switch[number[i][1] - 1] = 1
        else:
            switch[number[i][1] - 1] = 0

cnt = 0
for i in switch:
    print(i, end=" ")
    cnt += 1
    if cnt == 20:
        print("")
        cnt = 0
