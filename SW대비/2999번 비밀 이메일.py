# 2999번 비밀 이메일

message = input()
length = len(message)
R = 0
C = 0
for i in range(1, length+1):
    if length % i == 0:
       if i <= length//i:
           R = i
           C = length//i
       else:
           break
board = [[0] * C for _ in range(R)]


alpha = 0
for i in range(C):
    for j in range(R):
        board[j][i] = message[alpha]
        alpha  +=1

email = ""
for i in range(R):
    for j in range(C):
        email += board[i][j]
print(email)

