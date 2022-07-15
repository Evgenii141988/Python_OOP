def choose_sum_int_numbers(lst: list):
    result = []
    for i in lst:
        try:
            result.append(int(i))
        except ValueError:
            continue
    return sum(result)


if __name__ == '__main__':
    lst_in = input().split()
    print(choose_sum_int_numbers(lst_in))
