# 백준 2178번 미로 탐색
# https://www.acmicpc.net/problem/2178
'''
test case

4 6
101111
101010
101011
111011
'''

def maze_check(r_idx, c_idx, arr, visited):
    n = len(arr)
    m = len(arr[0])
    x = [1, 0, -1, 0]
    y = [0, -1, 0, 1]
    visited[r_idx][c_idx] = 1
    q = []
    q.append(r_idx)
    q.append(c_idx)
    
    while q:
        r_idx = q.pop(0)
        c_idx = q.pop(0)
        for i in range(4):
            rx = r_idx + x[i]
            cy = c_idx + y[i]
            if 0 <= rx < n and 0 <= cy < m:
                if arr[rx][cy] == 1 and visited[rx][cy] == 0:
                    visited[rx][cy] = visited[r_idx][c_idx] + 1
                    q.append(rx)
                    q.append(cy)
                    if (rx == n-1) and (cy == m-1):
                        
                        return visited[rx][cy]


n, m = map(int, input().split())

arr = [ [int(i) for i in input()] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

res = maze_check(0, 0, arr, visited)
print(res)



# 다른 사람 코드
from collections import deque

n, m = map(int, input().split())
maze_map = [[0] * (m+2)]
visit = [[0] * (m+1) for _ in range(n+1)]

for _ in range(n):
    maze_map.append([0]+list(map(int, input()))+[0])

maze_map.append([0] * (m+2))

pos_calc = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]

q = deque()
q.append([1,1])
visit[1][1] = 1

maze_end_flag = False

while not maze_end_flag:
    now_row, now_col = q.popleft()

    for c_row, c_col in pos_calc:
        target_row = now_row+c_row
        target_col = now_col+c_col

        if maze_map[target_row][target_col] == 1 and visit[target_row][target_col] == 0:
            q.append([target_row, target_col])
            visit[target_row][target_col] = visit[now_row][now_col] + 1
        
        if target_row == n and target_col == m:
            maze_end_flag = True

print(visit[n][m])