def get_required_distance_to_increase_or_decrease_coverage(house_locations, towers_locations, d):
    house_locations.sort()
    towers_locations.sort()

    first_tower = towers_locations[0]
    last_tower = towers_locations[-1]

    first_house = house_locations[0]
    last_house = house_locations[-1]

    #left
    left_coverage = first_tower - d
    left_diff = left_coverage - first_house


    # right
    right_coverage = last_tower + d
    right_diff = last_house - right_coverage

    print(left_diff, right_diff)
    print(max(left_diff, right_diff))


def main():
    house_locations = [1,5]
    towers_locations = [2]
    d = 4
    
    get_required_distance_to_increase_or_decrease_coverage(house_locations, towers_locations, d)

main()