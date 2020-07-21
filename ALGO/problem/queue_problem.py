# 큐 문제 0721
# 백준 10845번 문제
'''
정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성

6
push 1
front
back
pop
front
back
'''

# import sys
# input = sys.stdin.readline

n = int(input())

que = [0 for i in range(10001)]

front = 0
rear = 0

for _ in range(n):
    command = input().split()

    if command[0] == 'push':
        que[rear] = command[1]
        rear += 1
    
    if command[0] == 'pop':
        if que[front] == 0:
            print(-1)
        else:
            print(que[front])
        
        front += 1
        if front > rear:
            rear = front
            
    if command[0] == 'size':
        print(rear - front)

    if command[0] == 'empty':
        if rear - front <= 0:
            print(1)
        else:
            print(0)

    if command[0] == 'front':
        if que[front]:
            print(que[front])
        else:
            print(-1)
    
    if command[0] == 'back':
        if que[front] == 0:
            print(-1)
        elif que[rear-1]:
            print(que[rear-1])
        else:
            print(-1)
