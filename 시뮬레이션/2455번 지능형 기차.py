# 2455번 지능형 기차

ans = 0
station = 0
for i in range(4):
    out, inn = map(int, input().split())
    station = station - out + inn
    if station > ans:
        ans = station
print(ans)
