class Food:
    def __init__(self, name: str, weight: (int, float), calories: int):
        self._name = name
        self._weight = weight
        self._calories = calories


class BreadFood(Food):
    def __init__(self, name: str, weight: (int, float), calories: int, white: bool):
        super().__init__(name, weight, calories)
        self._white = white


class SoupFood(Food):
    def __init__(self, name: str, weight: (int, float), calories: int, dietary: bool):
        super().__init__(name, weight, calories)
        self._dietary = dietary


class FishFood(Food):
    def __init__(self, name: str, weight: (int, float), calories: int, fish: str):
        super().__init__(name, weight, calories)
        self._fish = fish


if __name__ == '__main__':
    bf = BreadFood("Бородинский хлеб", 34.5, 512, False)
    sf = SoupFood("Черепаший суп", 520, 890.5, False)
    ff = FishFood("Консерва рыбная", 340, 1200, "семга")
