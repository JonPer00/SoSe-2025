from my_classes import Subject, Supervisor, Experiment

if __name__ == "__main__":
    supervisor = Supervisor("Anna", "Musterfrau")

    subject = Subject("Max", "Mustermann", "männlich", 30)

    subject.estimate_max_hr()

    experiment = Experiment("Leistungstest", "2025-04-07")

    experiment.add_subject(subject)
    experiment.add_supervisor(supervisor)

    print(experiment)