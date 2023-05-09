def get_sum(n):
    series = []
    for i in range(n):
        if i < 3:
            series.append(i)
        else:
            term = sum(series[i-3:i])
            series.append(term)
    return sum(series)

def main():
    n = 5
    total = get_sum(n)
    print(total)

main()