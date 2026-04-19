from datasets import load_dataset
import json

dataset = load_dataset("newfacade/LeetCodeDataset")

human_fields = ["question_id", "task_id", "problem_description", "starter_code", "difficulty", "tags"]

filtered_dataset = dataset.select_columns(human_fields)

just_want_training_data = filtered_dataset["train"]
result = just_want_training_data.to_list() # turns dataset object into a list of dicts


with open("output.json", "w") as file:
    json.dump(
        result,
        file,
        indent=2
    )
