class SmartPhone:
    def __init__(self, model: str):
        self.model = model
        self.apps = []

    def add_app(self, app: object):
        if not any([isinstance(app, type(app_in)) for app_in in self.apps]):
            self.apps.append(app)

    def remove_app(self, app: object):
        self.apps.remove(app)


class AppVK:
    def __init__(self, name: str = "ВКонтакте"):
        self.name = name


class AppYouTube:
    def __init__(self, memory_max: int, name: str = "YouTube"):
        self.name = name
        self.memory_max = memory_max


class AppPhone:
    def __init__(self, phone_list: dict, name: str = "Phone"):
        self.name = name
        self.phone_list = phone_list


if __name__ == '__main__':
    sm = SmartPhone("Honor 1.0")
    sm.add_app(AppVK())
    sm.add_app(AppVK())  # второй раз добавляться не должно
    sm.add_app(AppYouTube(2048))
    for a in sm.apps:
        print(a.name)