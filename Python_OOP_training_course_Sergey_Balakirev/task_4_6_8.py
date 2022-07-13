class RetriveMixin:
    def get(self, request: dict):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request: dict):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request: dict):
        return "PUT: " + request.get('url')


class GeneralView:
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')

    def render_request(self, request: dict):
        if request['method'] not in self.allowed_methods:
            raise TypeError(f"Метод {request.get('method')} не разрешен.")
        method_request = request.get('method').lower()
        return self.__getattribute__(method_request)(request)


class DetailView(RetriveMixin, UpdateMixin, GeneralView):
    allowed_methods = ('GET', 'POST', 'PUT')


if __name__ == '__main__':
    view = DetailView()
    # html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'GET'})
    html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'PUT'})
    print(html)  # GET: https://stepik.org/course/116336/