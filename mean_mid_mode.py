from collections import Counter

def find_mean(numbers):
    n = len(numbers)
    mean = 0
    for i in numbers:
        mean += int(i) / n
        mean = round(mean, 2)
    return mean

def find_mid (numbers):
    numbers = sorted(numbers)

    n = len(numbers)
    is_even = n % 2 == 0
    mid = n // 2

    if is_even:
        sum = int(numbers[mid]) + int(numbers[mid-1])
        median = round(sum/2, 2)
    else:
        median = int(numbers[mid])
    return median

def find_mode (numbers):
    numbers = sorted(numbers)
    n = len(numbers)

    # find the maximum frequency
    maximum_freq = 0
    for i in range(n):
        count = 0
        for j in range(i, n):
            if numbers[i] == numbers[j]:
                count += 1
        if count > maximum_freq:
            maximum_freq = count

    mode = []    # elements that are equal to maximum frequncy
    for i in range(n):
        count = 0
        for j in range(i, n):
            if numbers[i] == numbers[j]:
                count += 1
        if count == maximum_freq:
            mode += [str(numbers[i])]
    return " ".join(mode)

numbers = "1 88 2 3 4 5 6 2 22 33 33 2 88  88 88 88  99 2 99 99 99 99 2 22 33".split()

# print(find_mean(numbers))
# print(find_mid(numbers))
print(find_mode(numbers))
# find_mode(numbers)