from abc import ABC, abstractmethod


class Model(ABC):

    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return f"Базовый класс Model"


class ModelForm(Model):
    __ID = 0

    def __init__(self, login: str, password: str):
        ModelForm.__ID += 1
        self._id = ModelForm.__ID
        self._login = login
        self._password = password

    def get_pk(self):
        return self._id


if __name__ == '__main__':
    form = ModelForm("Логин", "Пароль")
    print(form.get_pk())
