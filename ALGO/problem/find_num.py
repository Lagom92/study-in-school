# 나머지와 몪이 같은 수 구하기
# 0713

'''
숫자 N 이 주어질때,

나머지와 몫이 같은 자연수의 합

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


# 강사님 풀이 1
'''
규칙: (n+1), (n+1)*2, (n+1)*3, ... (n+1)*(n-1)

i: 1, 2, 3, ... (n-1)
'''
n = int(input())
res = 0
for i in range(1, n):
    res += (n+1)*i
print(res)


# 강사님 풀이 2
'''
가우스 합 = n(n+1)/2

i를 모두 더한 후 (n+1)를 곱해도 결과는 같다.

for 루프를 사용 x
'''
n = int(input())
res = n*(n-1)*(n+1)/2
print(res)