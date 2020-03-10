# 9517번 아이러브크로아티아

K = int(input())
problem_time = 210
for i in range(int(input())):
    time, result = input().split()
    time = int(time)
    problem_time -= time

    if problem_time <= 0:
        print(K)
        break
    if result == "T":
        if K <= 7:
            K += 1
        elif K >= 8:
            K = 1
