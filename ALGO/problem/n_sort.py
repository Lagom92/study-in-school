# 수 정렬하기_0722
# https://www.acmicpc.net/problem/2750

'''
버블 정렬
삽입 정렬
선택 정렬
'''

# 버블 정렬
def buble_sort(n, n_list):
    for i in range(n-1):
        for j in range(n-1-i):
            if n_list[j] > n_list[j+1]:
                n_list[j], n_list[j+1] = n_list[j+1], n_list[j]

    return n_list

# 삽입 정렬
def insertion_sort(n, n_list):
    for i in range(n):
        for j in range(i, 0, -1):
            if n_list[j] < n_list[j-1]:
                n_list[j], n_list[j-1] = n_list[j-1], n_list[j]
        
    return n_list

# 선택 정렬
def select_sort(n, n_list):
    for i in range(n-1):
        min_val = n_list[i]
        min_idx = i
        for j in range(i, n):
            if n_list[j] < min_val:
                min_val = n_list[j]
                min_idx = j
        n_list[i], n_list[min_idx] = n_list[min_idx], n_list[i]

    return n_list


n = int(input())
n_list = []
for _ in range(n):
    n_list.append(int(input()))
print(n, n_list)


# 버블 정렬 출력
res = buble_sort(n, n_list)
for i in res:
    print(i)


# 삽입 정렬 출력
res = insertion_sort(n, n_list)
for i in res:
    print(i)


# 선택 정렬 출력
res = select_sort(n, n_list)
for i in res:
    print(i)