class Aircraft:
    def __init__(self, model: str, mass: (int, float), speed: (int, float), top: (int, float)):
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    def __setattr__(self, key, value):
        if key == '_model' and not isinstance(value, str):
            raise TypeError('неверный тип аргумента')
        elif key in ('_mass', '_speed', '_top') and (not isinstance(value, (int, float)) or value <= 0):
            raise TypeError('неверный тип аргумента')
        elif key == '_chairs' and (not isinstance(value, int) or value <= 0):
            raise TypeError('неверный тип аргумента')
        elif key == '_weapons' and not isinstance(value, dict):
            raise TypeError('неверный тип аргумента')
        else:
            super().__setattr__(key, value)


class PassengerAircraft(Aircraft):
    def __init__(self, model: str, mass: (int, float), speed: (int, float), top: (int, float), chairs: int):
        super().__init__(model, mass, speed, top)
        self._chairs = chairs


class WarPlane(Aircraft):
    def __init__(self, model: str, mass: (int, float), speed: (int, float), top: (int, float), weapons: dict):
        super().__init__(model, mass, speed, top)
        self._weapons = weapons


if __name__ == '__main__':
    planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
              PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
              WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
              WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]