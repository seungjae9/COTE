# 10163번 색종이

N = int(input())
paper = []
for i in range(N):
    paper.append(list(map(int, input().split())))

board = [[0] * 101 for _ in range(101)]

for i in range(N):
    for j in range(paper[i][0], paper[i][0] + paper[i][2]):
        for x in range(paper[i][1], paper[i][1] + paper[i][3]):
            board[j][x] = i + 1

for i in range(N):
    res = 0
    for j in range(101):
        res += board[j].count(i+1)
    print(res)
