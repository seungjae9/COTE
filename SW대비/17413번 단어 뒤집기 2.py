# 17413번 단어 뒤집기 2

char = input()
N = len(char)
check = 0
while check != N-1:
    temp = []
    if char[check] == "<":
        for i in range(check, N-1):
            temp.append(char[i])
            check += 1
            if char[check] == ">":
                break
        print(temp)
    elif char[check] != "<":
        for i in range(check, N-1):
            temp.append(char[i])
            check += 1
            if char[check] == "<":
                break
        print(temp)




# [2기_광주_1반/박승재]


# res = []
#
# temp = []
# temp2 = []
# for i in range(len(char)):
#     if char[i] != "<":
#         temp.append(char[i])
#     if char[i] == " ":
#         res.append(temp)
#         temp = []

# print(res)
# print(temp)
