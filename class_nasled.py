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
