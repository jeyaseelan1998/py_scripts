n = int(input())

alpha = 'abcdefghijklmnopqrstuvwxyz'

col = 1
for row_num in range(1, n+1):
    right_idx = 0
    left = ""
    right = ""
    left_space = "  " * (n-row_num)
    for col_num in range(1, col+1):
        # print(row_num, col_num)
        if col_num <= row_num:
            left += alpha[col_num-1] + ","
            if row_num == 1 and col_num == 1:
                left = left.strip(',')
        else:
            right = alpha[right_idx] + "," + right
            right_idx += 1
    col += 2
    print(left_space+ left + right[:-1])

col = 2*n -3
for row_num in range(1, n):
    right_idx = 0
    left = ""
    right = ""
    left_space = "  " * (row_num)
    for col_num in range(1, col+1):
        if col_num <= n - row_num:
            left += alpha[col_num-1] + ","
            if row_num == n-1 and col_num == 1:
                left = left.strip(',')
        else:
            right = alpha[right_idx] + "," + right
            right_idx += 1
    col -= 2
    print(left_space+ left + right.strip(',') )