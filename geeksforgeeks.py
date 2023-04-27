arr = [1,3,2]

n = len(arr)

new_list = []
for i in range(n):
    cur_num = arr[i]
    left_part = arr[0:i]
    right_part = arr[i+1:n]
    # print(left_part, cur_num,right_part)
    

    min_1 = min(left_part) if len(left_part) else cur_num
    min_2 = min(right_part) if len(right_part) else cur_num

    idx_1 = arr.index(min_1)
    idx_2 = arr.index(min_2)

    is_small = min(cur_num, min_1, min_2) == cur_num
    if is_small:
        new_list.append(-1)
    elif min_1 == min_2:
        if idx_1<idx_2:
            new_list.append(idx_1)
        else:
            new_list.append(idx_2)
    else:
        if min_1 < min_2:
            new_list.append(idx_1)
        else:
            new_list.append(idx_2)

print(new_list)