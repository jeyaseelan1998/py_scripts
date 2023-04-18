alphabets = "abcdefghijklmnopqrstuvwxyz"
def char_position(char):
    return alphabets.find(char)

def encripted_pswd(word, s, e, d):
    word = list(word)
    for i in range(s, e+1):
        if word[i] == "a" and d == -1:
            word[i] = "z"
        elif word[i] == "z" and d == 1:
            word[i] = "a"
        else:
            word[i] = chr(ord(word[i]) + d)
    return "".join(word)



pswd = input()
n = int(input())

for i in range(n):
    instruction = list(map(int, input().split()))
    # print(instruction)
    start_idx = instruction[0]
    end_idx = instruction[1]
    dir = instruction[2]
    pswd = encripted_pswd(pswd, start_idx, end_idx, dir)
    print(pswd)