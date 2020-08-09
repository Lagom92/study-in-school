# 회전하는 큐
# https://www.acmicpc.net/problem/1021
'''
deque() 사용

test case
10 3
1 2 3
'''
from collections import deque

n, m = map(int, input().split())
target_lst = list(map(int, input().split()))
num_lst = deque(range(1, n+1))

res = 0
for target in target_lst:
    cnt = 0
    if num_lst[0] == target:
        num_lst.popleft()
    else:
        if num_lst.index(target) <= len(num_lst)//2:
            while target != num_lst[0]:
                num = num_lst.popleft()
                num_lst.append(num)
                cnt += 1
        else:
            while target != num_lst[0]:
                num = num_lst.pop()
                num_lst.insert(0, num)
                cnt += 1
        num_lst.popleft()
    res += cnt
print(res)



# 다른사람 코드
'''
rotate(n) 사용
요소들(elements)을 n값 만큼 회전 해주는 메소드 
n의 값이 음수(negative)이면 왼쪽으로 회전하고, n의 값이 양수이면 오른쪽으로 회전
'''
from collections import deque

n, m = map(int, input().split())
target_list = map(int, input().split())
q_list = deque([i for i in range(1, n+1)])

result = 0

for target_num in target_list: 
    pull_cnt = q_list.index(target_num)
    push_cnt = len(q_list) - pull_cnt

    if pull_cnt < push_cnt:
        result += pull_cnt
        q_list.rotate(-pull_cnt)
    else:
        result += push_cnt
        q_list.rotate(push_cnt)
    
    q_list.popleft()

print(result)