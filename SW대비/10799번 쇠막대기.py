# 10799번 쇠막대기

stick = input()


front = 0
back = 0

stack = []

def cal(stack):
    print(stack)
    


for i in stick:
    if i == "(":
        front += 1
        stack.append(i)
    elif i == ")":
        back += 1
        stack.append(i)
    if front == back:
        cal(stack)
        stack = []