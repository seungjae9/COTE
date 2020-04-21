# 16198번 에너지 모으기

# 양옆 가장 큰거 찾기 /// 만약에 가장 큰 값이 두개 라면 가운데 값이 더 작은 쪽을 선택 /// 당연히 양 끝은 선택 하면 안되고

N = int(input())
bead = list(map(int, input().split()))

res = 0
for cnt in range(N-2):
    maxval = 0
    idx = 0
    for i in range(1, len(bead)-1):
        if maxval < bead[i-1] * bead[i+1]:
            maxval = bead[i-1] * bead[i+1]
            idx = i
        elif maxval == bead[i-1] * bead[i+1]:
            if bead[i] < bead[idx]:
                idx = i
    del bead[idx]
    res += maxval
print(res)