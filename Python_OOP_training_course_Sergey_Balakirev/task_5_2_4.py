def get_sum(a, b):
    try:
        return int(a) + int(b)
    except:
        try:
            return float(a) + float(b)
        except:
            return a + b


if __name__ == '__main__':
    a, b = input().split()
    print(get_sum(a, b))
