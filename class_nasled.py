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