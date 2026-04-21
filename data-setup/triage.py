# End Goal: 
# After yanking data into a output.json using import.py...


import json
import subprocess
import os

def main():
    clone_repos()

    repo_paths = define_repo_paths()

    found = []

    with open("output.json", "r") as f: # openleetcode dataset
        leetcode_dataset = json.load(f) # as a list of dicts

    slug_to_id = {} # generates a dict of slug to id
    for problem in leetcode_dataset:
        slug = problem["task_id"]
        qid = problem["question_id"]
        slug_to_id[slug] = str(qid)

    id_to_difficulty = {} # generates a dict of id to difficulty
    for problem in leetcode_dataset:
        difficulty = problem["difficulty"]
        qid = problem["question_id"]
        id_to_difficulty[str(qid)] = difficulty



    # populate found with the question id of every .py file
    for author, path in repo_paths.items(): # turns repo_paths into list of tuples
        for root, dirs, files in os.walk(path): # os.walk yields current_dir, subdirs, files_in_dir
            for filename in files:
                if filename.endswith(".py"):
                    qid = extract_id(filename) # call function to get filename
                
                    if qid is not None:
                        found.append({
                            "question_id": qid,
                            "author": author,
                            "file": os.path.join(root, filename)
                        })
                    else:
                        stem = filename.replace(".py", "").lower().replace("_","-") # unify with leetcode_dataset
                        qid = slug_to_id.get(stem)
                        if qid is not None:
                            found.append({
                                "question_id": qid,
                                "author": author,
                                "file": os.path.join(root, filename)
                            })

    # triage found to only include files in output.json
    for problem in found:
        human_qid = problem["question_id"]
        problem["difficulty"] = id_to_difficulty.get(human_qid) # get can return None, so it gets filtered here. Errorsafe way to index into a dict

    buckets = {
        "Easy": {"yuri": [], "fisher": [], "cnkyrpsgl": [], "qiyuangong": [], "kamyu": []},
        "Medium": {"yuri": [], "fisher": [], "cnkyrpsgl": [], "qiyuangong": [], "kamyu": []},
        "Hard": {"yuri": [], "fisher": [], "cnkyrpsgl": [], "qiyuangong": [], "kamyu": []},
    }

    # populate buckets!
    for problem in found:
        difficulty = problem.get("difficulty")
        author = problem["author"]
        if difficulty in buckets:
            buckets[difficulty][author].append(problem) # append the dict holding id,author,file,difficulty

   # for difficulty, authors in buckets.items(): 
    #    print(difficulty)
     #   for author, problems in authors.items():
      #      print(f"{author}: {len(problems)} problems")


    # round robin!
    triaged_easy = round_robin(buckets["Easy"])
    triaged_medium = round_robin(buckets["Medium"])
    triaged_hard = round_robin(buckets["Hard"])

    final = {
        "easy": triaged_easy,
        "medium": triaged_medium,
        "hard": triaged_hard,
    }

    with open("triaged.json", "w") as f:
        json.dump(final, f, indent=2)


### now, triage round robin

    


def clone_repos():
    repos = [
    ("yuri", "https://github.com/YuriSpiridonov/LeetCode"),
    ("fisher", "https://github.com/fishercoder1534/Leetcode"),
    ("cnkyrpsgl", "https://github.com/cnkyrpsgl/leetcode"),
    ("qiyuangong", "https://github.com/qiyuangong/leetcode"),
    ("kamyu", "https://github.com/kamyu104/LeetCode-Solutions"),
    ]

    os.makedirs("repos", exist_ok=True) # exist_ok=True just doesn't throw an error if the dir already exists

    for author, url in repos: # list of tuples is 0, 1 as author, url
        dest = f"repos/{author}"
        if not os.path.exists(dest):
            subprocess.run(["git", "clone", "--depth=1", url, dest])
        else:
            print(f"{author} exists")



def define_repo_paths():
    repo_paths = {}
    for author in os.listdir("repos"): # indexes as a list of strings
        path = f"repos/{author}" # string of the dir
        repo_paths[author] = path

    return repo_paths

def extract_id(filename):
    # isolate just the question_id in the filename
    stem = filename.replace(".py", "") # cut the .py

    digits = ""

    for char in stem:
        if char.isdigit():
            digits += char
        else:
            break

    if len(digits) == 0:
        return None
        
    return(str(int(digits)))

    
def round_robin(difficulty_dict):
    result = []
    seen_ids = set()

    while len(result) < 33:
        for author, problems in difficulty_dict.items(): # problems is a list of dicts, entries of problems
            if len(result) >= 33:
                break
            while len(problems) > 0:
                problem = problems.pop(0)
                if problem["question_id"] not in seen_ids:
                    result.append(problem)
                    seen_ids.add(problem["question_id"])
                    break
    return result


        



main()