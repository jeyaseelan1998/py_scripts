n = int(input())

for i in range(1, 2*n):
    if i == 1 or i == (2*n - 1):
        star = "* " * 4
    else:
        star = "* " + ("  " * 2) + "* "
    
    if i <= n:
        left_space = "  " * (n - i)
    else:
        left_space = "  " * (i - n)
    
    print(left_space + star)