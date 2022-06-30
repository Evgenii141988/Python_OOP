import re


class StringText:
    def __init__(self, lst_words: list):
        self.lst_words = lst_words

    def __lt__(self, other: object):
        if not isinstance(other, StringText):
            raise TypeError('Объекты сравнения должны иметь тип StringText')
        return len(self.lst_words) < len(other.lst_words)

    def __le__(self, other: object):
        if not isinstance(other, StringText):
            raise TypeError('Объекты сравнения должны иметь тип StringText')
        return len(self.lst_words) <= len(other.lst_words)


def get_list_words(string: str) -> list:
    """Преобразует строку в список слов"""
    return re.findall(r'[А-Яа-я]+', string)


if __name__ == '__main__':
    stich = ["Я к вам пишу – чего же боле?",
             "Что я могу еще сказать?",
             "Теперь, я знаю, в вашей воле",
             "Меня презреньем наказать.",
             "Но вы, к моей несчастной доле",
             "Хоть каплю жалости храня,",
             "Вы не оставите меня."]
    lst_text = []
    for string in stich:
        lst_text.append(StringText(get_list_words(string)))
    lst_text_sorted = sorted(lst_text, reverse=True)
    lst_text_sorted = [' '.join(obj.lst_words) for obj in lst_text_sorted]
