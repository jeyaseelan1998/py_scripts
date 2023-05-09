def get_consecutive_array(array):
    array.sort()
    n = len(array)
    consecutives = [[array[0]]]
    for i in range(1, n):
        curr_num = array[i]
        for j in range(len(consecutives)):
            prev_num = consecutives[j][-1]
            if (curr_num - prev_num) == 1:
                consecutives[j].append(curr_num)
        if (curr_num - prev_num) != 1:
            consecutives.append([curr_num])

        # return consecutives
        group_of_consecutives = []
        for group in consecutives:
            group_of_consecutives.append(len(group))
        
    return consecutives, group_of_consecutives

def main():
    # array = [1,2,3,4,5,8,9,44,45,46,47]   #[[1,2,3,4,5], [8,9], [44,45,46,47]]
    array = list(map(int, input().split()))
    
    consecutives, group_of_consecutives = get_consecutive_array(array)

    print(consecutives)
    print(group_of_consecutives)

main()

