class Teacher:
    def __init__(self, name_teacher, education, experience):
        self._name_teacher = name_teacher
        self._education = education
        self._experience = experience

    def get_name_teacher(self):
        return self._name_teacher

    def get_education(self):
        return self._education

    def get_experience(self):
        return self._experience

    def set_experience(self, experience):
        self._experience = experience

    def get_teacher_data(self):
        return f"Преподаватель - {self._name_teacher}, образование {self._education}, опыт работы {self._experience} лет"

    def add_mark(self, name_student, marks):
        self._name_student = name_student
        self._marks = marks
        return f"{self._name_teacher}, поставил(а) оценку {self._marks} студенту {self._name_student}"

    def remove_mark(self, name_student, marks):
        self._name_student = name_student
        self._marks = marks
        return f"{self._name_teacher}, удалил(а) оценку {self._marks} студенту {self._name_student}"

    def give_a_consultation(self, class_of_students):
        self._class_of_students = class_of_students
        return f"{self._name_teacher} провел(а) консультацию в классе {self._class_of_students}"

class DisciplineTeacher(Teacher):
    def __init__(self, name_teacher, education, experience, discipline, job_title):
        super().__init__(name_teacher, education, experience)
        self._discipline = discipline
        self._job_title = job_title

    def get_discipline(self):
        return self._discipline

    def set_discipline(self, discipline):
        self._discipline = discipline

    def get_job_title(self):
        return self._job_title

    def set_job_title(self, job_title):
        self._job_title = job_title

    def get_teacher_data(self):
        return (f"Преподаватель - {self._name_teacher}, образование {self._education}, опыт работы {self._experience} лет "
                f"\nПредмет: {self._discipline}, Должность {self._job_title}")

    def add_mark(self, name_student, marks):
        super().add_mark(name_student, marks)
        return (f"{self._name_teacher}, поставил(а) оценку {self._marks} студенту {self._name_student}, "
                f"\nПредмет: {self._discipline}")

    def remove_mark(self, name_student, marks):
        super().remove_mark(name_student, marks)
        return (f"{self._name_teacher}, удалил(а) оценку {self._marks} студенту {self._name_student}"
                f"\nПредмет: {self._discipline}")

    def give_a_consultation(self, class_of_students):
        super().give_a_consultation(class_of_students)
        return (f"{self._name_teacher} провел(а) консультацию в классе {self._class_of_students} "
                f"\nпо предмету {self._discipline} как {self._job_title}")

teacher_1 = Teacher("Иван Петров", "КемГУ", 5)
print(teacher_1.get_teacher_data())
print(teacher_1.add_mark("Сидоров Коля", 2))
print(teacher_1.remove_mark("Мухамеджонов Игнат", 3))
print(teacher_1.give_a_consultation("5В"))
print()
teacher_2 = DisciplineTeacher("Мария Ивановна", "МГУ", 20, "Математика", "Учитель")
print(teacher_2.get_teacher_data())
print()
print(teacher_2.add_mark("Зайцев Павел", 5))
print()
print(teacher_2.remove_mark("Зимин Дмитрий", 4))
print()
print(teacher_2.give_a_consultation("6Г"))