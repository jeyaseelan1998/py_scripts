# 4
# 192.1.a.21    invalid
# 100.3.01.100
# 2001:12af:0:0000:19A:85a3:8a2e:03
# 12345:34ab:619:0000:0000:2AdD invalid

def is_primary_id(string):
    parts = string.split('.')
    if len(parts) != 4:
        return False
    for each_part in parts:
        if not each_part.isdigit():
            return False
        
        num = int(each_part)
        if num < 0 or num > 255:
            return False
    return True

def is_secondary_id(string):
    parts = string.split(':')
    if len(parts) != 8:
        return False
    for each_part in parts:
        if len(each_part) < 1 or len(each_part) > 4:
            return False
        for char in each_part:
            if char.isdigit():
                if int(char) < 0 or int(char) > 9:
                    return False
            elif char.lower() not in "abcdef":
                return False
    return True
    
n = int(input())
for i in range(n):
    string  = input()
    if not (is_primary_id(string) or is_secondary_id(string)):
        print(string)