from datetime import date

class Person():
    def __init__(self, first_name, last_name, birthdate):
        self.first_name = first_name
        self.last_name = last_name
        self.__birthdate = birthdate

    def get_age(self):
        """Berechnet das Alter basierend auf dem Geburtsdatum"""
        today = date.today()
        birth = date.fromisoformat(self.__birthdate)
        return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Subject(Person):
    def __init__(self, first_name, last_name, birthdate, sex):
        super().__init__(first_name, last_name, birthdate)
        self.sex = sex
        self.max_hr = None  # maximale Herzfrequenz

    def estimate_max_hr(self):
        """Schätzt die maximale Herzfrequenz (220 - Alter)"""
        self.max_hr = 220 - self.get_age()
        return self.max_hr

    def __str__(self):
        return f"Subject: {super().__str__()}, Geschlecht: {self.sex}, Max HF: {self.max_hr}"


class Supervisor(Person):
    def __init__(self, first_name, last_name, birthdate):
        super().__init__(first_name, last_name, birthdate)

    def __str__(self):
        return f"Supervisor: {super().__str__()}"


class Experiment():
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.subjects = []
        self.supervisors = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def add_supervisor(self, supervisor):
        self.supervisors.append(supervisor)

    def __str__(self):
        subject_list = "\n".join(str(s) for s in self.subjects)
        supervisor_list = "\n".join(str(s) for s in self.supervisors)
        return (f"Experiment: {self.name} ({self.date})\n"
                f"Supervisoren:\n{supervisor_list}\n"
                f"Testpersonen:\n{subject_list}")