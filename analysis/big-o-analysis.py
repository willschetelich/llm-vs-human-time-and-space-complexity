import json
import big_o
import anthropic

with open("testing.json") as f:
    testing_data = json.load(f)

for p in testing_data:
    if p['question_id'] == 100:
        problem = p

with open("easy/100/easy_100_qiyuangong.py") as f:
    solution_source = f.read()

