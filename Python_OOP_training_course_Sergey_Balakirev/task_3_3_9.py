class Recipe:
    def __init__(self, *args):
        self.ingredients = list(args)

    def add_ingredient(self, ing: object):
        self.ingredients.append(ing)

    def remove_ingredient(self, ing: object):
        self.ingredients.remove(ing)

    def get_ingredients(self):
        return tuple(self.ingredients)

    def __len__(self):
        return len(self.ingredients)


class Ingredient:
    def __init__(self, name: str, volume: float, measure: str):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f'{self.name}: {self.volume}, {self.measure}'


if __name__ == '__main__':
    recipe = Recipe()
    recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
    recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
    recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
    ings = recipe.get_ingredients()
    print(ings)
    n = len(recipe)  # n = 3
    print(n)
