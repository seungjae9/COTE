# 10158번 개미

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

board = [[0] * (w + 1) for _ in range(h+1)]


# 방향 결정하기
# 맨처음 오른쪽 대각선 위
direction = 0

# 순환


for time in range(t):
    # 처음부터 오른쪽 대각선 위로 움직일때
    if direction == 0:
        if h - q > 0 and p + 1 < w + 1:
            q += 1
            p += 1
        if h - q == 0 and p + 1 < w + 1:
            direction = 5

        else:
            break
    # elif direction ==
print(p, q)


board[h-q][p] = "1"
for i in range(len(board)):
    print(board[i])



