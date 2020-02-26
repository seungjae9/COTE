# 1547번 공

ball = [1, 2, 3]
for i in range(int(input())):
    X, Y = map(int, input().split())
    a = ball.index(X)
    b = ball.index(Y)
    ball[a] = Y
    ball[b] = X
print(ball[0])


# ball[a], ball[b] = ball[b], ball[a] 이런식으로 해도 될듯