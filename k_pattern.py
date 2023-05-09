n = int(input())

for i in range(n):
    left = "  " * i
    hallow = "  " * (n - 1 - i)

    print(left + "* " + hallow + "* ")
    
for i in range(n-1):
    left = "  " * (n-2-i)
    hallow = "  " * (i+1)

    print(left + "* " + hallow + "* ")
