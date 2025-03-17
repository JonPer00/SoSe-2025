from datetime import date
from typing import Dict, List, Any

def create_experiments(first_experiment_id: int, num_experiments: int = 10) -> List[Dict[str, Any]]:
    today = date.today()
    experiments: List[Dict[str, Any]] = []
    even_ids: int = 0

    try:
        first_experiment_id = int(first_experiment_id)
    except ValueError:
        print("Bitte nur Zahlen verwenden")
        return []

    for i in range(10):
        experiment_id = first_experiment_id + i
        if experiment_id % 2 == 0:
          even_ids +=1

        experiment = {
            "id": experiment_id,
            "experimenter": "Johnn",
            "creation_date": today,
            "test_name": f"Leistungstest {i+1}"
        }
        experiments.append(experiment)
    print(f"Es wurden {even_ids} gerade ID´s gefunden")
    return experiments

def display_experiments(experiments: List[Dict[str, Any]], num_to_display: int = 5) -> None:
    """Gibt die ersten fünf Experimente aus."""
    for i in range(min(num_to_display, len(experiments))):
        print(experiments[i])
first_experiment_id = 187

experiments_list = create_experiments(first_experiment_id)

if experiments_list:
    display_experiments(experiments_list)
