from datasets import load_dataset
import json

dataset = load_dataset("newfacade/LeetCodeDataset")

testing_fields = ["question_id", "prompt", "starter_code", "input_output", "test"]

filtered_dataset = dataset.select_columns(testing_fields)

just_want_training_data = filtered_dataset["train"]
result = just_want_training_data.to_list() # turns dataset object into a list of dicts


with open("testing.json", "w") as file:
    json.dump(
        result,
        file,
        indent=2
    )

