iSharp = list(input().split())

change = []
for i in range(1, len(iSharp)):
    temp = ""
    alpha = ""
    for j in range(len(iSharp[i])-1):
        if iSharp[i][j] == "[":
            temp += "]"
        elif iSharp[i][j] == "]":
            temp += "["
        elif iSharp[i][j] == "*":
            temp += "*"
        elif iSharp[i][j] == "&":
            temp += "&"
        else:
            alpha += iSharp[i][j]
    change.append(temp)
    change.append(alpha)

for i in range(0, len(change)-1, 2):
    print(iSharp[0] + change[i][::-1]+ " " + change[i+1]+ ";")

