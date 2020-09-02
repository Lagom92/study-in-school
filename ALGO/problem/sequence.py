# 백준 1588번 수열
# https://www.acmicpc.net/problem/1588

'''
시간 초과....왜?!!

수정 필!
'''

# import sys
# input = sys.stdin.readline

number = input()
left = int(input())
right = int(input())
N = int(input())

for _ in range(N):
    res = ''
    for num in number:
        if len(res) <= right:
            if num == '1':
                res += '132'
            elif num == '2':
                res += '211'
            else:
                res += '232'
        else:
            break
    number = res
    

number = number[left:right+1]
print(number)
cnt_1 = number.count('1')
cnt_2 = number.count('2')
cnt_3 = number.count('3')

print(cnt_1, cnt_2, cnt_3)

