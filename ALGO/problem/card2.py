# 백준 2164번 카드2
# https://www.acmicpc.net/problem/2164

from collections import deque

n = int(input())
box = deque(list(range(1, n+1)))

while len(box) >= 2:
    box.popleft()
    val = box.popleft()
    box.append(val)

print(box[0])
