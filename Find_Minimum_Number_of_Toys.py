prices = list(map(int, input().split()))
print("\n")
n = len(prices)

highest = max(prices)
lowest = min(prices)
required = [highest, lowest]

# from left
c = 0

left = 0
right = 0

taken_1 = 0

for idx in range(n):
    if c == 2:
        c = 0
        break
    if c < 1:
        left += 1
    if prices[idx] in required:
        c += 1
    taken_1 += 1
print(taken_1, " toys taken ot from left\n")

# from right
taken_2 = 0

for idx in range(len(prices)-1, -1, -1):
    if c == 2:
        c = 0
        break
    if c < 1:
        right += 1
    if prices[idx] in required:
        c += 1
    taken_2 += 1
print(taken_2, " toys taken ot from right\n")

print(left + right, " toys taken ot from both\n")

min = min(taken_1, taken_2, left + right)

print(min, " is minimum\n")

print(n - min, " is available is self.\n")

