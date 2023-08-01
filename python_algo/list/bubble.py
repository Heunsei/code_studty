def bubble_sort(numbers):
    for i in range(len(numbers)-1, 0, -1):
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                tmp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = tmp
                print(numbers)

numbers = [55, 7, 78 ,12, 42]

print(bubble_sort(numbers))
