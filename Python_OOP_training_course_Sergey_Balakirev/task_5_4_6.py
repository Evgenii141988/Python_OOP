class DateString:
    def __init__(self, date_string: str):
        self.check_date(date_string)
        self.day, self.month, self.year = (int(elm) for elm in date_string.split('.'))

    def check_date(self, date: str):
        date_lst = [elm for elm in date.split('.')]
        if len(date_lst) == 3 and all((elm.isdigit() for elm in date_lst)):
            day, month, year = (int(elm) for elm in date_lst)
            if not (1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 3000):
                raise DateError("Неверный формат даты")
        else:
            raise DateError("Неверный формат даты")

    def __str__(self):
        return f'{self.day:02}.{self.month:02}.{self.year:04}'


class DateError(Exception):
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message


if __name__ == '__main__':
    date_string = input()
    try:
        date = DateString(date_string)
        print(date)
    except DateError as de:
        print(de)