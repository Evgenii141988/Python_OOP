def convert_int_float_type(elm):
    try:
        return int(elm)
    except ValueError:
        try:
            return float(elm)
        except ValueError:
            return elm


if __name__ == '__main__':
    lst_in = input().split()
    lst_out = list(map(convert_int_float_type, lst_in))
    print(lst_out)
