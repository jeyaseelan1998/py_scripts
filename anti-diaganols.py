m, n = input().split()
m, n = int(m), int(n)

matrix = []
for i in range(m):
    row = input().split()
    matrix.append(row)

for i in range(n):
    # print(i)
    col = i
    row = 0
    while row < m and row <= i:
        # print(row, col, end="  ")
        print(matrix[row][col], end="  ")
        row += 1
        col -= 1
    print()

for i in range(1, m):
    # print(i)
    col = n-1
    row = i
    while row < m and col >= 0:
        # print(row, col, end="  ")
        print(matrix[row][col], end="  ")
        row += 1
        col -= 1
    print()