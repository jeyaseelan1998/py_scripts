IDs_list = input().split()

n = len(IDs_list)

# get unique sorted ids in same ORDER
unique_IDs_list = []
for index, id in enumerate(IDs_list):
    id = "".join(sorted(id))
    if id not in unique_IDs_list:
            unique_IDs_list.append(id)
print(unique_IDs_list)

# get unique sorted ids group. i.e, same manufacturer
unique_IDs_dict = {}
for id in unique_IDs_list:
    count = 0
    for item in IDs_list:
        item = "".join(sorted(item))
        if id == item:
            count += 1
    unique_IDs_dict[id] = count
print(unique_IDs_dict)

# update key in uniqe_ids_dict 
for id in unique_IDs_list:
    for item in IDs_list:
        sorted_item = "".join(sorted(item))
        if id == sorted_item:
            val = unique_IDs_dict[sorted_item]
            del unique_IDs_dict[sorted_item]
            unique_IDs_dict[item] = val
            break
print(unique_IDs_dict)