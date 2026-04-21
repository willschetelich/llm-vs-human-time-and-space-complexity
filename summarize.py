import os
import pathlib
llm_win = 0
human_win = 0
same = 0



# iterate through easy, qid, and every qid-report.md


for root, dirs, files in os.walk("."):
    for filename in files:
        if filename.endswith("-report.md"):
            path = os.path.join(root, filename)
            with open(path, "r") as f:
                content = f.read()
            if "Superior algorithm: Same" in content:
                same = same+1
            if "Superior algorithm: Claude" in content:
                llm_win = llm_win+1
            if "Superior algorithm: Human" in content:
                human_win = human_win+1

print(f" Humans Win: {human_win}, \n LLM Win: {llm_win},\n tie: {same}")
# tally points for claude, human, same

# print to ROOT / summary.md


