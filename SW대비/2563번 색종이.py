# 2563번 색종이

N = int(input())
location = []
for i in range(N):
    location.append(list(map(int, input().split())))

board = [[0]* 100 for _ in range(100)]
for i in range(N):
    for j in range(-location[i][1]-9, -location[i][1]+1):
        for x in range(location[i][0]-1, location[i][0]+9):
            board[j][x] = 1
res = 0
for i in range(len(board)):
    res += sum(board[i])
print(res)


