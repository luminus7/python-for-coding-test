'''
2021.1.13. SJLEE
# N, K 
# select what to do between work1&2
# work1. N - 1
# work2. N / K iff. result of step1 can be divided by K, with no remainder.
# do above procedures until N become 1.
# goal: calculate minimum number of works until N: 1.
# e.g., N: 17, K:4 -> (1)work1. 17-1 -> (2)work2. 16//4 -> (3)work3. 4//4 ... 1 => output: 3 times

# Key Idea: Divide as much as possible (최소 시행 횟수를 위해서 최대한 많이 나누어야 함) - greedy sol
'''

N, K = map(int,input().split())

count = 0

# while N >= 1:   # 이게 더 안정적인 코드일듯.
while N != 1:
    if N%K == 0:
        N = N/K     # N/K available
        count += 1
    else:
        N -= 1      # N/K not available, do N-1
        count += 1

print(count)

'''
# python에는 do-while loop가 없기 때문에... (코드 구조)
# 출처: https://woogyun.tistory.com/519

```c [do-while in C]
do:
    task()
while condition
```

```py [writing task() part twice ... Hassle]
task()
while condition:
    task()
```

```py [GOOD.. but condition in if is in reversed form] => dongbin Na's pick
while True:
    task()
    if not condition: break
```

```py [GOOD in readability ... Preferred one]
while True:
    task()
    if condition: continue
    break
```
'''

'''
# original from dongbin Na 3/5.py
# 왜 이렇게 짠거지..
n, k = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # K로 나누기
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)
'''

'''
# original from dongbin Na 3/6.py
# 취향 드러나는 참신한 구성
n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
'''