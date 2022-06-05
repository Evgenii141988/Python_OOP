# Подвиг 11. Объявите класс с именем Translator (для перевода с английского на русский) со следующими методами:
# add(self, eng, rus) - для добавления новой связки английского и русского слова (если английское слово уже существует,
# то новое русское слово добавляется как синоним для перевода, например, go - идти, ходить, ехать);
# remove(self, eng) - для удаления связки по указанному английскому слову;
# translate(self, eng) - для перевода с английского на русский (метод должен возвращать список из русских слов,
# соответствующих переводу английского слова, даже если в списке всего одно слово).
# Создайте экземпляр tr класса Translator и вызовите метод add для следующих связок:
# tree - дерево
# car - машина
# car - автомобиль
# leaf - лист
# river - река
# go - идти
# go - ехать
# go - ходить
# milk - молоко
# Затем, методом remove() удалите связку для английского слова car. С помощью метода translate() переведите слово go.
# Результат выведите на экран в виде строки из всех русских слов, связанных со словом go:
# Вывод в формате: идти ехать ходить

class Translator:
    dictionary = {}

    def add(self, eng, rus):
        self.dictionary.setdefault(eng, []).append(rus)

    def remove(self, eng):
        del self.dictionary[eng]

    def translate(self, eng):
        return self.dictionary[eng]


words = ['tree дерево', 'car машина', 'car автомобиль', 'leaf лист', 'river река',
         'go идти', 'go ехать', 'go ходить', 'milk молоко']

if __name__ == '__main__':
    tr = Translator()
    for word in words:
        eng, rus = word.split()
        tr.add(eng, rus)
    tr.remove('car')
    print(*tr.translate('go'))

