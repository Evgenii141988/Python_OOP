class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    def __init__(self, methods=('GET',)):
        GenericView.__init__(self, methods)

    def render_request(self, request: dict, method: str):
        if not (method in self.methods):
            raise TypeError('данный запрос не может быть выполнен')
        return self.__getattribute__(method.lower())(request)

    def get(self, request: dict):
        if not isinstance(request, dict):
            raise TypeError('request не является словарем')
        if not ('url' in request):
            raise TypeError('request не содержит обязательного ключа url')
        return f"url: {request['url']}"


if __name__ == '__main__':
    dv = DetailView()
    print(dv.__dict__)
    html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')
    print(html)
