class PhoneNumber:
    def __init__(self, number: int, fio: str):
        self.number = number
        self.fio = fio

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value: int):
        if self.check_number(value):
            self.__number = value

    @staticmethod
    def check_number(number):
        return isinstance(number, int) and len(str(number)) == 11


class PhoneBook:
    def __init__(self, *args):
        self.numbers = list(args)

    def add_phone(self, phone):
        self.numbers.append(phone)

    def remove_phone(self, indx):
        self.numbers.pop(indx)

    def get_phone_list(self):
        return self.numbers


if __name__ == '__main__':
    p = PhoneBook()
    p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
    p.add_phone(PhoneNumber(21345678901, "Панда"))
    phones = p.get_phone_list()
    print(phones)
