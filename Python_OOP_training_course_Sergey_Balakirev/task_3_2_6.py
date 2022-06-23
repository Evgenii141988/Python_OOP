class RenderList:
    def __init__(self, type_list):
        self.type_list = type_list

    def __setattr__(self, key, value):
        if value not in ("ul", "ol"):
            value = "ul"
        super().__setattr__(key, value)

    def __call__(self, lst_menu, *args, **kwargs):
        html_string = ''
        for item in lst_menu:
            html_string += f'<li>{item}</li>\n'
        return f'<{self.type_list}>\n{html_string}</{self.type_list}>'


if __name__ == '__main__':
    lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
    render = RenderList("ol")
    html = render(lst)
    print(html)
