a=input()

color_count_dict = {}
for color in a:
    count = a.count(color)
    color_count_dict[color] = count

quantity_list = sorted(set(color_count_dict.values()), reverse = True)

new_list = []
for qty in quantity_list:
    row = []
    for key, val in color_count_dict.items():
        if qty == val:
            row += [key] * val
    new_list.extend(list(reversed(row)))           

print("".join(new_list))