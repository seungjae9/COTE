# 14502번 연구소

# 조합으로 벽 세우는데 구하기(0, 0, 0 인데 좌표 찾아서 조합 3개 구하기)
# 벽세우고 bfs 돌리기

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

