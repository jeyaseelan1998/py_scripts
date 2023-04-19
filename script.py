def findProduct(num_list):
    length = len(num_list)

    if length == 0:
        return 0
    else:
        product = 1
        for num in num_list:
            product *= int(num)
        return product

# list_a = [2, 3, 4, 2, 6, 4]
#   2 x 3 x 4 = 24  list_a[:3]
#   6 x 4   = 24    list_a[4:]
#  mid point is 3, so element 2 is output

num_list = input().split()

length = len(num_list)

for i in range(length):
    left_side_product = findProduct(num_list[:i])
    right_side_product = findProduct(num_list[i+1:])

    if left_side_product == right_side_product:
        print(i)
        break
