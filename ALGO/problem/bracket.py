# 백준 9012 괄호
# https://www.acmicpc.net/problem/9012

'''
입력 bracket 중 에 '()'를 전부 제거하고 
남은게 없으면 'YES' 출력
남은게 있으면 'NO' 출력
'''
n = int(input())
for _ in range(n):
    bracket = input()
    while "()" in bracket:
        bracket = bracket.replace("()", "")
        
    # print(bracket)
    if len(bracket) == 0:
        print("YES")
    else:
        print("NO") 
