import shutil
import os
import json

with open("triaged.json", "r") as f:
    result = json.load(f)

for difficulty in result:
    for entry in result[difficulty]:
        src = entry["file"]
        qid = entry["question_id"]
        author = entry["author"]
        dest_dir = f"{difficulty}/{qid}"

        os.makedirs(dest_dir, exist_ok=True)
        shutil.copy(src, f"{dest_dir}/{difficulty}_{qid}_{author}.py")

        

