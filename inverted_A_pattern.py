n = int(input())

if n % 2 == 0:
    mid = n // 2
else:
    mid = n // 2 + 1
    
k = 2*n - 3

for i in range(1, n+1):
    left_space = "  " * (i-1)
    hallow_space = "  " * k
    if i == n:
        print(left_space + "* " + hallow_space)
    elif i == mid:
        hallow_space = "* " * k
        print(left_space + "* " + hallow_space + "*")
    else:
        print(left_space + "* " + hallow_space + "*")
    k -= 2