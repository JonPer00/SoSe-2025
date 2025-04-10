from leistungstest import estimate_max_hr

class Person:
    def __init__(self, first_name, last_name, dateofbirth):
        self.first_name = first_name
        self.last_name = last_name
        self.__dateofbirth = dateofbirth  # privates Attribut

    def get_dateofbirth(self):
        """Gibt das Geburtsdatum zurück"""
        return self.__dateofbirth

class Subject(Person):
    def __init__(self, first_name, last_name, dateofbirth, sex):
        super().__init__(first_name, last_name, dateofbirth)
        self.sex = sex

    def estimate_max_hr(self):
        """Schätzt den maximalen Puls basierend auf dem Geburtsdatum"""
        return estimate_max_hr(self.get_dateofbirth())

class Supervisor(Person):
    def __init__(self, first_name, last_name, dateofbirth):
        super().__init__(first_name, last_name, dateofbirth)

class Experiment:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.subjects = []
        self.supervisors = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def add_supervisor(self, supervisor):
        self.supervisors.append(supervisor)