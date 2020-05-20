# 2164번 카드2


from collections import deque
N = int(input())
q = deque([i+1 for i in range(N)])
for case in range(N-1):
    q.popleft()
    q.append(q.popleft())
print(q[0])