class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.password = psw
        self.port = port

    def connect(self):
        print(f'соединение с БД: {self.user}, {self.password}, {self.port}')

    def close(self):
        print(f'Закрытие соединения с БД')

    def read(self):
        return f'Данные из БД'

    def write(self, data):
        print(f'Записть в БД: {data}')


if __name__ == '__main__':
    db = DataBase('root', '1234', 80)
    db2 = DataBase('root2', '5678', 40)
    print(id(db), id(db2))
    db.connect()
    db2.connect()
