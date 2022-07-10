class StringDigit(str):
    def __init__(self, string: str):
        self.__check_string(string)
        super().__init__()

    def __check_string(self, string: str):
        if not all((i.isdigit() for i in string)):
            raise ValueError("в строке должны быть только цифры")

    def __add__(self, other: str):
        self.__check_string(other)
        return StringDigit(super().__add__(other))

    def __radd__(self, other: str):
        return StringDigit(other).__add__(self)


if __name__ == '__main__':
    sd = StringDigit("123")
    print(sd)  # 123
    sd = sd + "456"  # StringDigit: 123456
    print(sd)
    print(type(sd))
    sd = "789" + sd  # StringDigit: 789123456
    print(sd)
    print(type(sd))
