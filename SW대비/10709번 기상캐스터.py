# 10709번 기상캐스터

H, W = map(int, input().split())
sky = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        time = 0
        if sky[i][j] == "c":
            sky[i][j] = time
            for x in range(j+1, W):
                if sky[i][x] == ".":
                    time += 1
                    sky[i][x] = time
                else:
                    break
        elif sky[i][j] == ".":
            sky[i][j] = -1

for i in range(H):
    print(" ".join(map(str, sky[i])))