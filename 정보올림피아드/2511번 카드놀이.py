# 2511번 카드놀이

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_score = 0
B_score = 0
res = ""
check = []
for i in range(10):
    if A[i] > B[i]:
        A_score +=3
        if A_score >= B_score:
            res = "A"
    elif A[i] < B[i]:
        B_score +=3
        if A_score <= B_score:
            res = "B"
    else:
        A_score +=1
        B_score +=1
        check.append("D")

if len(check) == 10:
    print(A_score, B_score)
    print("D")
else:
    print(A_score, B_score)
    print(res)
