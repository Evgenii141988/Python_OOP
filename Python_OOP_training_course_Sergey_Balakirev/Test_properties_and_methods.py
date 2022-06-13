class Server:
    """
    для описания работы серверов в сети
    Соответственно в объектах класса Server должны быть локальные свойства:
    buffer - список принятых пакетов (изначально пустой);
    ip - IP-адрес текущего сервера.
    """
    gen_ip = (i for i in range(1, 100))

    def __init__(self):
        self.ip = next(Server.gen_ip)
        self.buffer = []
        self.connect = False
        self.router_connect = None

    def send_data(self, data):
        """
        для отправки информационного пакета data (объекта класса Data)
        с указанным IP-адресом получателя (пакет отправляется роутеру и
        сохраняется в его буфере - локальном свойстве buffer)
        """
        self.router_connect.buffer.append(data)

    def get_data(self):
        """
        возвращает список принятых пакетов (если ничего принято не было,
        то возвращается пустой список) и очищает входной буфер
        """
        data_packages = self.buffer.copy()
        self.buffer.clear()
        return data_packages

    def get_ip(self):
        """возвращает свой IP-адрес"""
        return self.ip


class Router:
    """
    для описания работы роутеров в сети (в данной задаче полагается один роутер).
    И одно обязательное локальное свойство (могут быть и другие свойства):
    buffer - список для хранения принятых от серверов пакетов (объектов класса Data).
    """

    def __init__(self):
        self.buffer = []
        self.servers_connect = {}

    def link(self, server):
        """для присоединения сервера server (объекта класса Server) к роутеру"""
        self.servers_connect.setdefault(server.ip, server)
        server.router_connect = self
        server.connect = True
        print('Сonnection established successfully')

    def unlink(self, server):
        """для отсоединения сервера server (объекта класса Server) от роутера"""
        del self.servers_connect[server.ip]
        server.router_connect = None
        server.connect = False
        print('Сonnection stopped')

    def send_data(self):
        """
        для отправки всех пакетов (объектов класса Data) из буфера роутера
        соответствующим серверам (после отправки буфер должен очищаться)
        """
        for data in self.buffer:
            if data.ip in self.servers_connect:
                self.servers_connect[data.ip].buffer.append(data)
            else:
                print('Нет подключения к необходимому серверу')
        self.buffer.clear()


class Data:
    """
    для описания пакета информации
    Наконец, объекты класса Data должны содержать, два следующих локальных свойства:
    data - передаваемые данные (строка);
    ip - IP-адрес назначения.
    """

    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


if __name__ == '__main__':
    router = Router()
    sv_from = Server()
    router.link(sv_from)
    router.link(Server())
    router.link(Server())
    sv_to = Server()
    router.link(sv_to)
    sv_from.send_data(Data("Hello", sv_to.get_ip()))
    router.send_data()
    sv_to.send_data(Data("Hi", sv_from.get_ip()))
    router.send_data()
    msg_lst_from = sv_from.get_data()
    msg_lst_to = sv_to.get_data()
    print(msg_lst_from)
    print(msg_lst_to)