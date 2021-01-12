'''
2021.1.12. SJLEE
# N x M cards. N: #rows, M: #cols
# select the row, then pick the card with smallest value.
# input is given in line by line manner.
# goal: pick up the most large value.
'''


'''
print("N, M :")
# select row and col
N, M = map(int, input().split())

# dynamically create 2-dimensional list
_list = list()
for row in range(N):
    _list[][col].extend(list(map(int,input().split()))) # 한 list에 list를 concatenate하는 연산
    #_list.append(int(input()))                   # 한 list에 한 값을 추가하는 연산
    #_list += [[0]*M]                             # 두 list를 합치는 연산 , *는 반복 연산자
print("len: ", len(_list))
print("_list = ", _list)
'''

print("N, M :")
# select row and col
N, M = map(int, input().split())

# dynamically create 2-dimensional list
_list = list()
for col in range(M):
    _list = [ [] for row in range(N)]   # List comprehension

for row in range(N):
    _list[row].extend(list(map(int,input().split())))
# input().split()을 통해 한 줄씩 받고
# map(int, ~)을 통해 한 줄을 통째로 int 변환
# list(~~)을 통해 explicit하게 형 변환
# _list[0], _list[1], _list[2]에 각각의 list를 extend해 줌
# initial _list는 비어있는 리스트

for row in range(N):
    print(_list[row])

result = 0
for row in range(N):
    min_tmp = min(_list[row])   # list를 int로 형변환 해 주는듯.
    result = max(min_tmp, result)

print(result)

'''
# not working code section
result = 101
for data in _list:
    result = min(result, data)
print(result)
'''

'''
# original from dongbin Na
# 단일 for문, 한 줄 입력받을 때 마다 min value찾기
# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력 받아 확인하기
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력
'''

'''
# original from dongbin Na
# 이중 for문, 한 줄 입력받을 때 마다 min value찾기
# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력 받아 확인하기
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력
'''