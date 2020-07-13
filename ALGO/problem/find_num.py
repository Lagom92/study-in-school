# 나머지와 몪이 같은 수 구하기
# 0713

'''
숫자 N

num // N 와 num % N 이 같은 모든 자연수의 합 ??

ex)
N=1, 0
N=2, 3
N=3, 12
N=4, 30
'''

N = int(input())
res = 0
for i in range(N+1, N**2):
    if i//N == i%N:
        res += i

print(res)