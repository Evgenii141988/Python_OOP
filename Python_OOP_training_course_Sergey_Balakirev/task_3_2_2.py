from random import randint, choice


def random_password(psw_chars: str, min_length: int, max_length: int):
    def inner():
        len_password = randint(min_length, max_length)
        password = ''
        while len(password) < len_password:
            password += choice(psw_chars)
        return password

    return inner


class RandomPassword:
    def __init__(self, psw_chars: str, min_length: int, max_length: int):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        len_password = randint(self.min_length, self.max_length)
        password = ''
        while len(password) < len_password:
            password += choice(self.psw_chars)
        return password


if __name__ == '__main__':
    min_length = 5
    max_length = 20
    psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
    rnd1 = random_password(psw_chars, min_length, max_length)
    chars = "qwertyuiopasdfghjklzxcvbnm1234567890!@#$%"
    rnd = RandomPassword(chars, 8, 20)
    lst_pass = [rnd() for _ in range(3)]
    print(lst_pass)