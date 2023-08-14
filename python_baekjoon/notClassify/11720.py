number = int(input())
numbers = list(input())

result = 0

for num in range(number):
    result += int(numbers[num])
    
print(result)
