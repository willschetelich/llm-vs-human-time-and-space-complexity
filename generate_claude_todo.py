import json
import os

def main():
    with open("triaged.json", "r") as f:
        result = json.load(f)

    ### generate a list of all the question_ids

    all_easy_question_ids = generate_qid_list(result, "easy")
    all_medium_question_ids = generate_qid_list(result, "medium")
    all_hard_question_ids = generate_qid_list(result, "hard")

    # print(all_easy_question_ids)

    # create dirs
    os.makedirs("easy", exist_ok=True)
    os.makedirs("medium", exist_ok=True)
    os.makedirs("hard", exist_ok=True)

    prepare_claude(all_easy_question_ids, "easy")
    prepare_claude(all_medium_question_ids, "medium")
    prepare_claude(all_hard_question_ids, "hard")


def generate_qid_list(result, difficulty):
    id_list = []
    for problem in result[difficulty]:
        id_list.append(problem["question_id"])
    
    return id_list


def prepare_claude(qid_list, difficulty):
    with open("output.json", "r") as f:
        big_json = json.load(f)

    for qid in qid_list:
        for p in big_json:
            if qid == str(p["question_id"]):
                problem = p
                break
        else:
            continue #


        os.makedirs(f"{difficulty}/{qid}", exist_ok=True)

        with open(f"{difficulty}/{qid}/{qid}.json", "w") as f:
            json.dump(problem, f, indent=2)

        with open(f"{difficulty}/{qid}/{qid}-claude.py", "w") as f:
            f.write("")

        
        



main()
