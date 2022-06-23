class HandlerGET:
    def __init__(self, func):
        self.__func = func

    def __call__(self, request, *args, **kwargs):
        return self.get(self.__func, request)

    def get(self, func, request, *args, **kwargs):
        if 'method' not in request or request['method'] == 'GET':
            return f'GET: {func(request)}'
        return None


@HandlerGET
def contact(request):
    return "Сергей Балакирев"


if __name__ == '__main__':
    res = contact({"method": "GET", "url": "contact.html"})
    print(res)
