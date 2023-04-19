# 1322 -->   132231
# 465 --> 46564

number = list(input())
reversed_number = number[::-1]

i = 0
for num in reversed_number:
    if num != number[len(number)-1]:
        reversed_number = reversed_number[i:]
        break
    i += 1

number.extend(reversed_number)

new_number = "".join(number)

print(new_number)