class Router:
    app = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func


class Callback:
    def __init__(self, path: str, router_cls: object):
        self.path = path
        self.router_cls = router_cls

    def __call__(self, func):
        self.router_cls.add_callback(self.path, func)


@Callback('/', Router)
def index():
    print('index')
    return '<h1>Главная</h1>'


if __name__ == '__main__':

    route = Router.get('/')
    if route:
        ret = route()
        print(ret)
