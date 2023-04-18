
def decode(string):
    idx = ""
    word = ""
    for l in string:
        if l.isdigit():
            idx += l
        else:
            word += l
    return [int(idx), word]

def each_word (arr):
    return arr[1]

def main():
    words = "4park 1meet 3the 0Let's 2at".split()
    words = list(map(decode, words))

    words.sort()

    words = list(map(each_word, words))

    print(" ".join(words))

main()