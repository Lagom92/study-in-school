# 약수 구하기
'''
입력받은 숫자 N의 모든 약수를 출력하시오.

tes_case
Input
100

Output
1 2 4 5 10 20 25 50 100
'''


# 방법 1 for 루프 사용
N = int(input())
res = []

for i in range(1, N+1):
    if N % i == 0:
        res.append(i)

print(*res)