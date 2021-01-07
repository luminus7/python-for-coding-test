'''
2021.1.7. SJLEE
# N: 배열의 크기 | M: 숫자가 더해지는 횟수 |K: 연속으로 더할 수 있는 횟수
# e.g.,
# input 5, 8, 3
# input 2, 4, 5, 4, 6
# internal: 6+6+6+5+6+6+6+5
# output 46
'''
# N,M,K 입력
N, M, K = map(int, input().split())

# N개를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()
first = data[N-1]
second = data[N-2]

# solution1 중첩 반복문
result = 0

while True:
    for i in range(K):
        if M == 0:
            break
        result += first
        M -= 1
    if M == 0:
        break
    result += second
    M -= 1

'''
# solution2 숫자연산. 이게 더 좋은듯
count = int(m/(k+1)) * K
count += m%(K+1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m-count) * second # 두 번째로 큰 수 더하기
'''

print(result)


'''
# original from dongbin Na
# N, M, K를 공백을 기준으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N개의 수를 공백을 기준으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort() # 입력 받은 수들 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result) # 최종 답안 출력
'''