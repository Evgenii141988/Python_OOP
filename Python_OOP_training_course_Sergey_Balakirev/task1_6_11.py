class Viber:
    MESSAGES = []

    @classmethod
    def add_message(cls, msg):
        cls.MESSAGES.append(msg)

    @classmethod
    def remove_message(cls, msg):
        cls.MESSAGES.remove(msg)

    @staticmethod
    def set_like(msg):
        if msg.fl_like:
            msg.fl_like = False
        else:
            msg.fl_like = True

    @classmethod
    def show_last_message(cls, number):
        print(cls.MESSAGES[len(cls.MESSAGES) - number:])

    @classmethod
    def total_messages(cls):
        return len(cls.MESSAGES)


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like


if __name__ == '__main__':
    msg = Message("Всем привет!")
    Viber.add_message(msg)
    Viber.add_message(Message("Это курс по Python ООП."))
    Viber.add_message(Message("Что вы о нем думаете?"))
    Viber.add_message(Message("Что вы думаете?"))
    Viber.add_message(Message("Что вы о ней думаете?"))
    Viber.show_last_message(3)
    Viber.set_like(msg)
    Viber.remove_message(msg)