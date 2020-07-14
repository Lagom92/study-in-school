# 휴식을 위하여
'''
각 그늘이 독서에 적합한지 (공사 현장에서 R 이상 떨어진 그늘인지) 판별하는 코드를 작성하시오.
위치 (x, y) 가 공사 현장에서 R 이상 떨어져있다는 조건

공사 현장 위치 (a, b)
공사현장에서 R 만큼의 거리 미만은 독서에 적합 x

그늘이 N개 존재
각각의 그늘 위치는 (x_i, y_i)

원의 방정식을 이용
(x - a)^2 + (y - b)^2 >= R^2

test_case
Input
20 10 10
3
25 10
20 15
70 70

Output
noisy
noisy
silent
'''


x, y, R = map(int, input().split())

n = int(input())
for i in range(n):
    x_i, y_i = map(int, input().split())

    if (x-x_i)**2 + (y-y_i)**2 >= R**2:
        print("silent")
    else:
        print("noisy")