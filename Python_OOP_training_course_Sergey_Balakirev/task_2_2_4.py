class Car:
    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 100:
            self.__model = value


if __name__ == '__main__':
    car = Car()
    car.model = 'Toyota'
    print(car.__dict__)