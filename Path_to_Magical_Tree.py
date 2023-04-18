def find_HCF(arr):
    n = len(arr)
    minimum = min(arr)
    if n < 2:
        return minimum
    else:
        hcf = 1
        for i in range(2, minimum+1):
            factor = 0
            for num in arr:
                if num % i == 0:
                    factor += 1
            if factor == n:
                hcf = i
        return hcf


def main():
    numbers = list(map(int, input().split()))
    n = len(numbers)
    from_left = []
    from_right = []
    for i in range(1, n+1):
        from_left += [numbers[0:i]]
        from_right += [numbers[n-i:n]]

    total_groups = from_left + from_right

    route = []
    for grp in total_groups:
        route += [find_HCF(grp)]
    
    route = map(str,set(route))
    route = sorted(route, key=int)

    print(" ".join(route))


main()