# 16968번 차량 번호판 1

plate = input()
if plate[0] == "d":
    res = 10
elif plate[0] == "c":
    res = 26
for i in range(1, len(plate)):
    if plate[i] == "d" and plate[i-1] == "d":
        res *= 9
    elif plate[i] == "d" and plate[i-1] == "c":
        res *= 10
    elif plate[i] == "c" and plate[i-1] == "c":
        res *= 25
    elif plate[i] == "c" and plate[i-1] == "d":
        res *= 26

print(res)

