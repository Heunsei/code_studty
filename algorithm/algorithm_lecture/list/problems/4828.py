# min max
# N개의 양의 정수에서 가장 큰 수와 작은수의 차이

T = int(input())
for num in range(1, T+1):
    num_of_tc = int(input())
    numbers = list(map(int, input().split()))
    print(numbers)
    min_val = numbers[0]
    max_val = numbers[0]
    for val in numbers:
        if max_val < val:
            max_val = val
        if min_val > val:
            min_val = val
    result = max_val - min_val
    print(f'#{num} {result}')