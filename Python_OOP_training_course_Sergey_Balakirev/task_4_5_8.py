from abc import ABC, abstractmethod


class CountryInterface(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def population(self):
        pass

    @property
    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class Country(CountryInterface):
    def __init__(self, name: str, population: int, square: (int, float)):
        self.__name = name
        self.__population = population
        self.__square = square

    @property
    def name(self):
        return self.__name

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, value):
        self.__population = value

    @property
    def square(self):
        return self.__square

    @square.setter
    def square(self, value):
        self.__square = value

    def get_info(self):
        return f"{self.__name}: {self.__square}, {self.__population}"


if __name__ == '__main__':
    country = Country("USA", 333000000, 950005489.55)
    name = country.name
    pop = country.population
    country.population = 335000000
    country.square = 950005489
    print(country.get_info())  # Россия: 354005483.0, 150000000
