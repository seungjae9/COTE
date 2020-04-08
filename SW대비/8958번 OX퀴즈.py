# 8958번 OX퀴즈

for i in range(int(input())):
    quiz =  input()
    conti = 0
    ans = 0
    for j in quiz:
        if j == "O":
            conti +=1
        else:
            conti = 0
        ans += conti
    print(ans)