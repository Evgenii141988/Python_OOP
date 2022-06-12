class AppStore:
    APPS = []

    def add_application(self, app):
        self.APPS.append(app)

    def remove_application(self, app):
        self.APPS.remove(app)

    def block_application(self, app):
        app.blocked = True

    def total_apps(self):
        return len(self.APPS)


class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked


if __name__ == '__main__':
    store = AppStore()
    app_youtube = Application("Youtube")
    store.add_application(app_youtube)
    store.remove_application(app_youtube)
    store.block_application(app_youtube)
    print(app_youtube.blocked)
