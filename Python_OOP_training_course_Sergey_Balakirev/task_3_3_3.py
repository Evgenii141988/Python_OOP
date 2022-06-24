class Model:
    def __init__(self):
        self.data = {}

    def query(self, **kwargs):
        self.data = kwargs

    def __str__(self):
        if self.data:
            string = 'Model: '
            for key, value in self.data.items():
                string += f'{key} = {value}, '
            return string.strip(', ')
        return 'Model'


if __name__ == '__main__':
    model = Model()
    model.query(id=1, fio='Sergey', old=33)
    print(model)
