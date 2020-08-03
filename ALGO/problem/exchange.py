# 백준 5585번 거스름돈
# https://www.acmicpc.net/problem/5585


money = int(input())

change = 1000 - money

lst = [500, 100, 50, 10, 5, 1]

res = 0
for i in range(len(lst)):
    if change // lst[i] != 0:
        res += change // lst[i]
        change %= lst[i]
print(res)