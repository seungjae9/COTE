# # 2477번 참외밭

K = int(input())
field = [list(map(int, input().split())) for _ in range(6)]

width, idx = 0, 0
height, idx2 = 0, 0
for i in range(6):
    if field[i][0] == 1 and field[i][1] > width or field[i][0] == 2 and field[i][1] > width:
        width = field[i][1]
        idx = i
    if field[i][0] == 3 and field[i][1] > height or field[i][0] == 4 and field[i][1] > height:
        height = field[i][1]
        idx2 = i
minfield = field * 2
print((width*height - minfield[idx+3][1]*minfield[idx2+3][1]) * K)


