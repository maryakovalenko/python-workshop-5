numbers1 = [1, 5, 2, 3, 4, 6, 1, 7]
numbers2 = [1, 5, 2, 3, 4, 1, 7]

def max_number(numbers):
    max_number = min(numbers)
    while max_number + 1 in numbers:
        max_number += 1
    return max_number

def result(numbers):
    return [min(numbers), max_number(numbers)]

print(result(numbers1))
print(result(numbers2))