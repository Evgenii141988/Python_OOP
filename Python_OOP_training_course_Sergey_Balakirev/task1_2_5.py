# Подвиг 5. Объявите пустой класс с именем Car. С помощью функции setattr() добавьте в этот класс атрибуты:
# model: "Тойота"
# color: "Розовый"
# number: "О111АА77"
# Выведите на экран атрибут color, используя словарь __dict__ класса Car.

class Car:
    pass


if __name__ == '__main__':
    setattr(Car, 'model', "Тойота")
    setattr(Car, 'color', "Розовый")
    setattr(Car, 'number', "О111АА77")
    print(Car.__dict__['color'])
