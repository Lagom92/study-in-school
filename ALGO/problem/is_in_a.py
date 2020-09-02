# 백준 1920번 수 찾기
# https://www.acmicpc.net/problem/1920


'''
재귀 사용
이진 탐색 사용

f(찾는 값, 값 리스트, 시작 인덱스, 끝 인덱스)
가운데 가 찾는 값이면 리턴
찾는 값이 가운데 값보다 작으면 -> 끝 인덱스 변경 -> 다시 탐색
찾는 값이 가운데 값보다 크면 -> 시작 인덱스 변경 -> 다시 탐색
찾는 값이 리스트에 없는 경우 -> 탈출
'''
def is_in_a(target, lst, start_idx, end_idx):
    mid_idx = (start_idx + end_idx) // 2
    if start_idx > end_idx:
        return 0

    if target == lst[mid_idx]:
        return 1
    
    if target < lst[mid_idx]:       # 왼쪽
        return is_in_a(target, lst, start_idx, end_idx-mid_idx-1)
    else:       # 오른쪽
        return is_in_a(target, lst, start_idx+mid_idx, end_idx)

    return 0



n = int(input())
lst = list(map(int, input().split()))
lst.sort()
m = int(input())
target_lst = list(map(int, input().split()))
for target in target_lst:
    res = is_in_a(target, lst, 0, n-1)
    print(res)


