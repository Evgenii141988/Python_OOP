class Handler:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def __call__(self, func, *args, **kwargs):
        def wrapper(request, *args, **kwargs):
            if 'method' not in request or request['method'] in self.methods:
                return self.__getattribute__(request.get('method', 'get').lower())(func, request)
            return None

        return wrapper

    def get(self, func, request, *args, **kwargs):
        return f'GET: {func(request)}'

    def post(self, func, request, *args, **kwargs):
        return f'POST: {func(request)}'


@Handler(methods=('GET', 'POST'))  # по умолчанию methods = ('GET',)
def contact(request):
    return "Сергей Балакирев"


if __name__ == '__main__':
    res = contact({"method": "POST", "url": "contact.html"})
    res1 = contact({})
    print(res)
    print(res1)
