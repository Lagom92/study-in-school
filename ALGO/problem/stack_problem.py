# 스택 문제_0720
'''
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령의 총 5가지

push x: 정수 x를 스택에 넣는 연산

pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력 / 만약 스택에 들어있는 정수가 없는 경우 -1 출력

size: 스택에 들어있는 정수의 개수를 출력

empty: 스택이 비어있으면 1, 아니면 0 을 출력

top: 스택의 가장 위에 있는 정수를 출력, 만약 스택에 들어있는 정수가 없는 경우 -1 출력

Test Case
input           output
7               -1
pop             -1
top             123
push 123        123
top             -1
pop             -1
top
pop

'''


n = int(input())

box = []
cnt = 0

for _ in range(n):
    command = input().split()

    if command[0] == 'push':
        box.append(command[1])
        cnt += 1

    if command[0] == 'pop':
        if cnt >= 1:
            print(box.pop(-1))
            cnt = max(cnt-1, 0)
        else:
            print(-1)

    if command[0] == 'size':
        print(cnt)
        
    if command[0] == 'empty':
        print(0 if cnt else 1)
    
    if command[0] == 'top':
        print(box[-1] if cnt else -1)
