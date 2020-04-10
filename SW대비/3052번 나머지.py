# 3052번 나머지


remainder = {}
ans = 0
for i in range(10):
    number = int(input())
    if number % 42 not in remainder:
        remainder[number % 42]  = 1
        ans +=1
print(ans)
