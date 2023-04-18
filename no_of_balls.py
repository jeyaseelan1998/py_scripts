n = 9
numbers = "3 7 4 1 5 3 7 3 6".split()
numbers = list(map(int, numbers))

maximum = 0
for i in range(n):
    for j in range(i+2, n):
        product = min(numbers[i], numbers[j]) * (j-i)
        # print(product)
        if maximum < product:
            maximum = product

print(maximum)