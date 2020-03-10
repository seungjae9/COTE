secret = {
            'A' : '000000',
            'B' : '001111',
            'C' : '010011',
            'D' : '011100',
            'E' : '100110',
            'F' : '101001',
            'G' : '110101',
            'H' : '111010',
            }

N = int(input())
N6 = input()
letter = []
temp = ""
for i in N6:
    temp += i
    if len(temp) == 6:
        letter.append(temp)
        temp = ""

res = ""
ans = ""
for i in range(N):
    compare = letter[i]
    stop = 0
    for key, val in secret.items():
        check = 0
        for j in range(6):
            if compare[j] != val[j]:
                check += 1
        if check <= 1:
            stop = 1
            res += key
        if stop == 1:
            break
        if key == "H" and check >= 2:
            ans += str(i+1)
if len(ans) >= 1:
    print(ans[0])
else:
    print(res)

