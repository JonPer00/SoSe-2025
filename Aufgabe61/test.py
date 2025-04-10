from my_classes import Subject, Supervisor, Experiment

if __name__ == "__main__":
    supervisor = Supervisor("Anna", "Musterfrau", "1980-05-15")

    subject = Subject("Max", "Mustermann", "1995-03-22", "männlich")
    subject.estimate_max_hr()

    experiment = Experiment("Leistungstest", "2025-04-10")
    experiment.add_subject(subject)
    experiment.add_supervisor(supervisor)

    print(experiment)