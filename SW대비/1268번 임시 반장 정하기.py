# 1268번 임시 반장 정하기
N = int(input())

student = []
for i in range(N):
    student.append(list(map(int, input().split())))

classroom = [[[], [], [], [], [], [], [], [], []],
             [[], [], [], [], [], [], [], [], []],
             [[], [], [], [], [], [], [], [], []],
             [[], [], [], [], [], [], [], [], []],
             [[], [], [], [], [], [], [], [], []]]
for i in range(N):
    for j in range(5):
        classroom[j][student[i][j]-1].append(i+1)

res = []
for i in range(N):
    res.append([])


for i in range(N):
    for j in range(5):  # 학년 찾기
        for x in range(9):   # 반 찾기
            for t in range(len(classroom[j][x])):   # 학생 수 찾기
                if i+1 == classroom[j][x][t] and len(classroom[j][x]) >= 2:
                    for tt in range(len(classroom[j][x])):
                        if classroom[j][x][tt] not in res[i]:
                            res[i].append(classroom[j][x][tt])

total = 0
idx = 1
for i in range(N):
    if len(res[i]) > total:
        total = len(res[i])
        idx = i + 1
print(idx)
