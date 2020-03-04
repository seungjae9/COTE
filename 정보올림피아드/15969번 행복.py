# 15969번 행복

N = int(input())
score = list(map(int, input().split()))
print(max(score) - min(score))