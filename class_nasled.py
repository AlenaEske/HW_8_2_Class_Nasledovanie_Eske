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