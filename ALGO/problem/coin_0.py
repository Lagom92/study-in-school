# 백준 동전 0
# https://www.acmicpc.net/problem/11047

N, K = map(int, input().split())

coin_lst = []
for _ in range(N):
    coin_lst.append(int(input()))
coin_lst = coin_lst[::-1]

res = 0
for coin in coin_lst:
    res += K // coin
    K %= coin
    
print(res)
