class Course:
    def __init__(self, name: str):
        self.name = name
        self.modules = []

    def add_module(self, module: object):
        self.modules.append(module)

    def remove_module(self, indx: int):
        self.modules.pop(indx)


class Module:
    def __init__(self, name: str):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson: object):
        self.lessons.append(lesson)

    def remove_lesson(self, indx: int):
        self.lessons.pop(indx)


class LessonItem:
    def __init__(self, title: str, practices: int, duration: int):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        type_attr = {'title': str, 'practices': int, 'duration': int}
        if not isinstance(value, type_attr.get(key)):
            raise TypeError("Неверный тип присваиваемых данных.")
        super().__setattr__(key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item not in ('title', 'practices', 'duration'):
            super().__delattr__(item)


if __name__ == '__main__':
    course = Course("Python ООП")
    module_1 = Module("Часть первая")
    module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
    module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
    module_1.add_lesson(LessonItem("Урок 3", 5, 800))
    course.add_module(module_1)
    module_2 = Module("Часть вторая")
    module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
    module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
    course.add_module(module_2)
