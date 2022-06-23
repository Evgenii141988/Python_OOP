import re


class DigitRetrieve:
    def __call__(self, string: str, *args, **kwargs):
        if string.isdigit():
            return int(string)
        elif '-' in string and string.lstrip('-').isdigit() and '--' not in string:
            return int(string)
        return None


if __name__ == '__main__':
    dg = DigitRetrieve()
    d1 = dg("123")  # 123 (целое число)
    d2 = dg("45.54")  # None (не целое число)
    d3 = dg("-56")  # -56 (целое число)
    d4 = dg("12fg")  # None (не целое число)
    d5 = dg("abc")  # None (не целое число)
    d6 = dg("123-")
    d7 = dg("--56")
    print(d1, d2, d3, d4, d5, d6, d7)
    st = ["123", "abc", "-56.4", "0", "-5", "--56"]
    digits = list(map(dg, st))  # [123, None, None, 0, -5]
    print(digits)
