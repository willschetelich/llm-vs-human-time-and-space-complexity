import json
from pathlib import Path # Path is a class
import analysis

ROOT = Path(__file__).parent.parent # get root dir of project

def main():
    # dict with qid to testing entry
    qid_to_param_generation_data = {}
    testing_path = ROOT / "analysis" / "testing.json"
    if testing_path.exists():
        with open(testing_path) as f:
            for entry in json.load(f):
                qid = str(entry["question_id"])
                qid_to_param_generation_data[qid] = entry

    # loop over all problems in traiged.json

    with open(ROOT / "triaged.json") as f:
        triaged = json.load(f)
    
    all_problems = []
    for difficulty, problems in triaged.items(): # key value, difficulty, entries as list of dicts
        for problem in problems:
            all_problems.append({**problem, "difficulty": difficulty}) # buildling a new literal dict with new entry

    for problem in all_problems:
        qid = str(problem["question_id"])
        difficulty = problem["difficulty"]
        testing_entry = qid_to_param_generation_data.get(qid)

        # pass all this to analysis.py
        analysis.analyze_problem(qid, difficulty, testing_entry)
    # lastly, tally results
    # loop through all dirs with markdown files
    # in claude, human, same in easy, medium, and hard, and overall. Total percentages


main()