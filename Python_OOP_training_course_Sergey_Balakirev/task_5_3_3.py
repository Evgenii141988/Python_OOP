def input_int_numbers(str_num: str):
    try:
        numbers = tuple(int(i) for i in str_num.split())
    except:
        raise TypeError('все числа должны быть целыми')
    else:
        return numbers


if __name__ == '__main__':
    while True:
        try:
            string = input()
            numbers = input_int_numbers(string)
            print(*numbers)
            break
        except TypeError:
            continue
