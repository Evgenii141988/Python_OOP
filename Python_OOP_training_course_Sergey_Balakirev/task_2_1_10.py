import re
from random import choice, randint
from string import ascii_letters, digits


class EmailValidator:
    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def check_email(cls, email):
        reg = r'^[a-zA-Z_\d.]{0,100}@[a-zA-Z_\d\.]{1,50}\.[a-zA-Z_\d\.]{1,50}'
        if cls.__is_email_str(email):
            if re.fullmatch(reg, email) and '..' not in email and len(email) <= 151:
                return True
        return False

    @classmethod
    def get_random_email(cls):
        random_number = randint(1, 100)
        email = ''
        while len(email) <= random_number:
            letter = choice(ascii_letters + digits + '_.')
            email += letter
        return f'{email}@gmail.com'

    @staticmethod
    def __is_email_str(email):
        return isinstance(email, str)


if __name__ == '__main__':
    em = EmailValidator()
    res = EmailValidator.check_email("sc_lib@list.ru")  # True
    res1 = EmailValidator.check_email("sc_lib@list_ru")  # False
    print(res)
    print(res1)

