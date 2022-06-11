import re

class CardCheck:
    CHARS_FOR_NUMBER = r'\d{4}-\d{4}-\d{4}-\d{4}'
    CHARS_FOR_NAME = r'[A-Z]+\s[A-Z]+'

    @classmethod
    def check_card_number(cls, number):
        if re.fullmatch(cls.CHARS_FOR_NUMBER, number):
            return True
        return False

    @classmethod
    def check_name(cls, name):
        if re.fullmatch(cls.CHARS_FOR_NAME, name):
            return True
        return False


if __name__ == '__main__':
    is_number = CardCheck.check_card_number("1234-5678-9012-0000")
    is_name = CardCheck.check_name("SERGEI BALAKIREV")
