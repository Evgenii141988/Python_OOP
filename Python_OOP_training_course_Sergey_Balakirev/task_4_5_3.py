class Student:
    def __init__(self, fio: str, group: str):
        self._fio = fio
        self._group = group
        self._lect_marks = []  # оценки за лекции
        self._house_marks = []  # оценки за домашние задания

    def add_lect_marks(self, mark):
        self._lect_marks.append(mark)

    def add_house_marks(self, mark):
        self._house_marks.append(mark)

    def __str__(self):
        return f"Студент {self._fio}: оценки на лекциях: {str(self._lect_marks)}; оценки за д/з: {str(self._house_marks)}"


class Mentor:
    def __init__(self, fio: str, subject: str):
        self._fio = fio
        self._subject = subject


class Lector(Mentor):
    def __init__(self, fio: str, subject: str):
        super().__init__(fio, subject)

    def set_mark(self, student: object, mark: int):
        student.add_lect_marks(mark)

    def __str__(self):
        return f'Лектор {self._fio}: предмет {self._subject}'


class Reviewer(Mentor):
    def __init__(self, fio: str, subject: str):
        super().__init__(fio, subject)

    def set_mark(self, student: object, mark: int):
        student.add_house_marks(mark)

    def __str__(self):
        return f'Эксперт {self._fio}: предмет {self._subject}'


if __name__ == '__main__':
    lector = Lector("Балакирев С.М.", "Информатика")
    reviewer = Reviewer("Гейтс Б.", "Информатика")
    students = [Student("Иванов А.Б.", "ЭВМд-11"), Student("Гаврилов С.А.", "ЭВМд-11")]
    persons = [lector, reviewer]
    lector.set_mark(students[0], 4)
    lector.set_mark(students[1], 2)
    reviewer.set_mark(students[0], 5)
    reviewer.set_mark(students[1], 3)
    for p in persons + students:
        print(p)
