# 13458번 시험 감독

N = int(input())
stu = list(map(int, input().split()))
B, C = map(int, input().split())


cnt = 0
for i in range(N):
    stu[i] -= B
    cnt += 1
    if stu[i] > 0:
        if stu[i] % C == 0:
            cnt += stu[i] // C
        else:
            cnt += 1 + (stu[i] // C)

print(cnt)