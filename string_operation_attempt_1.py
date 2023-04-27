def get_max_value(str_list, condition):
    unique_words_list = list(set(str_list))
    frequency ={}
    for word in unique_words_list:
        if condition == "count":
            value = str_list.count(word)
        else:
            value = len(word)
        frequency[word] = value
    return max(frequency.values())

def print_word(str_list, value, condition):
    for word in str_list:
        count = str_list.count(word)
        if condition == "length" and len(word) == value:
            print(word)
            break
        if condition == "count" and count == value:
            print(word)
            break
            

string = "She plays carroms and he plays cricket at their place"

string = string.lower().split()

total_no_of_words = len(string)
max_frequency = get_max_value(string, "count")
print_word(string, max_frequency, "count")

max_length = get_max_value(string, "length")
print_word(string, max_length, "length")