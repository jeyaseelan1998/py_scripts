def findProduct(num_list):
    length = len(num_list)

    if length == 0:
        return 0
    else:
        product = 1
        for num in num_list:
            product *= int(num)
        return product

num_list = input().split()

length = len(num_list)

for i in range(length):
    left_side_product = findProduct(num_list[:i])
    right_side_product = findProduct(num_list[i+1:])

    if left_side_product == right_side_product:
        print(i)
        break
