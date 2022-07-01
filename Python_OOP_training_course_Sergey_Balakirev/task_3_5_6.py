    import re


    class Morph:
        def __init__(self, *args):
            self.__words = [word.strip(' .,!?:;').lower() for word in args]

        def add_word(self, word: str):
            if word not in self.__words:
                self.__words.append(word.lower())

        def get_words(self):
            return tuple(self.__words)

        def __eq__(self, other: str):
            if not isinstance(other, str):
                raise TypeError("Значение должно иметь тип str")
            return other.lower() in self.__words


    if __name__ == '__main__':
        dict_words = [Morph('связь', 'связи', 'связью', 'связей', 'связям', 'связями', 'связях'),
                      Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами',
                            'формулах'),
                      Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам',
                            'векторами', 'векторах'),
                      Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам',
                            'эффектами', 'эффектах'),
                      Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях')]
        text = input()
        text_lst = re.findall(r'[А-Яа-я]+', text)
        counter = sum(obj == word.lower() for word in text_lst for obj in dict_words)
        print(counter)