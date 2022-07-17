class Test:
    def __init__(self, descr: str):
        if not 10 <= len(descr) <= 10000:
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
        self.descr = descr

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):
    def __init__(self, descr: str, ans_digit: (int, float), max_error_digit: float = 0.01):
        super().__init__(descr)
        if not (isinstance(ans_digit, (int, float)) and isinstance(max_error_digit,
                                                                   (int, float)) and max_error_digit >= 0):
            raise ValueError('недопустимые значения аргументов теста')
        self.ans_digit = ans_digit
        self.max_error_digit = max_error_digit

    def run(self):
        ans = float(input())
        return self.ans_digit - self.max_error_digit <= ans <= self.ans_digit + self.max_error_digit


if __name__ == '__main__':
    descr, ans = map(str.strip, input().split('|'))  # например: Какое значение получится при вычислении 2+2? | 4
    ans = float(ans)  # здесь для простоты полагаем, что ans точно число и ошибок в преобразовании быть не может
    try:
        test = TestAnsDigit(descr, ans)
        print(test.run())
    except ValueError as v:
        print(v)

