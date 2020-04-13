# 13300번 방 배정

N, K = map(int, input().split())
classroom = {}
for i in range(N):
    A, B = input().split()
    if A + B not in classroom:
        classroom[A + B] = 1
    else:
        classroom[A + B] += 1

need = 0
for val in classroom.values():
    need += val // K
    if val % K > 0:
        need += 1


print(need)

