import anthropic
import re
import signal
try:
    import big_o
    BIG_O_AVAILABLE = True
except ImportError:
    BIG_O_AVAILABLE = False
import json
from pathlib import Path


NORMALIZE = {
    'o(1)': 'O(1)',
    'o(logn)': 'O(log n)',
    'o(log n)': 'O(log n)',
    'o(n)': 'O(n)',
    'o(nlogn)': 'O(n log n)',
    'o(n log n)': 'O(n log n)',
    'o(n^2)': 'O(n^2)',
    'o(n2)': 'O(n^2)',
    'o(n²)': 'O(n^2)',
    'o(n^3)': 'O(n^3)',
    'o(n3)': 'O(n^3)',
    'o(n³)': 'O(n^3)',
    'o(2^n)': 'O(2^n)',
}

def normalize_complexity(s):  # scraped from LLM
    if not s:
        return None
    s = re.split(r'\s+(?:where|excluding|amortized)\b', s, flags=re.IGNORECASE)[0].strip()
    key = re.sub(r'\s+', '', s).lower()
    return NORMALIZE.get(key, s)


def superior_algorithm(claude_res, human_res): # scraped from LLM
    order = ["O(1)", "O(log n)", "O(n)", "O(n log n)", "O(n^2)", "O(n^3)", "O(2^n)"]
    ct = normalize_complexity(claude_res["time"])
    ht = normalize_complexity(human_res["time"])
    ci = order.index(ct) if ct in order else 999
    hi = order.index(ht) if ht in order else 999
    if ci < hi:
        return "Claude"
    elif hi < ci:
        return "Human"
    else:
        return "Same"



EMPIRICAL_MAP = {
    'Constant': 'O(1)',
    'Logarithmic': 'O(log n)',
    'Linear': 'O(n)',
    'Linearithmic': 'O(n log n)',
    'Quadratic': 'O(n^2)',
    'Cubic': 'O(n^3)',
    'Polynomial': 'O(n^k)',
    'Exponential': 'O(2^n)',
}

client = anthropic.Anthropic()
ROOT = Path(__file__).parent.parent

def analyze_problem(qid, difficulty, testing_entry):
    # find human, find llm path, find qid.json
    human_llm_json = import_human_llm_json(difficulty, qid)
    if not human_llm_json:
        return

    # analyze with claude
    claude_human_verdict = claude_analysis(human_llm_json["human"], human_llm_json["json"])
    claude_llm_verdict = claude_analysis(human_llm_json["llm"], human_llm_json["json"])

    # analyze with big_o
    try:
        big_o_human_verdict = boa(human_llm_json["human"], human_llm_json["json"], testing_entry)
    except Exception as e:
        big_o_human_verdict = None

    try:
        big_o_llm_verdict = boa(human_llm_json["llm"], human_llm_json["json"], testing_entry)
    except Exception as e:
        big_o_llm_verdict = None


    #  build report in correct dir TODO

    conflict = "N/A"
    if big_o_human_verdict and big_o_human_verdict['time'] != claude_human_verdict['time']:
        conflict = "Disagree"
    elif big_o_human_verdict:
        conflict = "Agree"
    if big_o_llm_verdict and big_o_llm_verdict['time'] != claude_llm_verdict['time']:
        conflict = "Disagree"
    elif big_o_llm_verdict and conflict == "N/A":
        conflict = "Agree"
    if big_o_llm_verdict and big_o_human_verdict:
        if big_o_human_verdict['time'] == 'O(1)' and big_o_llm_verdict['time'] == 'O(1)':
            conflict = "Inconclusive"




    report_path = ROOT / difficulty / qid / f"{qid}-report.md"

    lines = [
        f"qid: {qid}",
        "",
        "LLM code:",
        f"Time: {claude_llm_verdict['time']} according to Claude",
        f"Space: {claude_llm_verdict['space']} according to Claude",
        "",
        "Human code:",
        f"Time: {claude_human_verdict['time']} according to Claude",
        f"Space: {claude_human_verdict['space']} according to Claude",
        "",
        f"big_o time (LLM): {big_o_llm_verdict['time'] if big_o_llm_verdict else 'N/A'}",
        f"big_o time (Human): {big_o_human_verdict['time'] if big_o_human_verdict else 'N/A'}",
        "",
        # id like to add to check if the big_o time agreed with the claude time
        f"big-o and claude {conflict}",
        "",
        f"Superior algorithm: {superior_algorithm(claude_llm_verdict, claude_human_verdict)}",
    ]

    with open(report_path, "w") as f:
        f.write("\n".join(lines) + "\n")
        

def import_human_llm_json(difficulty, qid):
    human_llm_json = {}

    llm_path = ROOT / difficulty / qid / f"{qid}-claude.py"
    json_path = ROOT / difficulty / qid / f"{qid}.json"

    human_path = None
    for file in (ROOT / difficulty / qid).iterdir():
        if file.suffix == ".py" and "claude" not in file.name:
            human_path = file
            break
    if not human_path:
        print("Error, no human code found")
        return None

    with open(llm_path) as f:
        llm_source = f.read()

    with open(human_path) as f:
        human_source = f.read()

    with open(json_path) as f:
        json_snippet = json.load(f)

    human_llm_json["human"] = human_source
    human_llm_json["llm"] = llm_source
    human_llm_json["json"] = json_snippet

    return human_llm_json

def claude_analysis(source, meta):
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=256,
            messages=[{
            "role": "user",  
            "content": ( # LLM produced a query it would like
                "Analyze the time and space complexity of this solution.\n\n"
                f"Problem:\n{meta['problem_description'][:600]}\n\n"
                f"Starter code:\n{meta['starter_code']}\n\n"
                f"Solution:\n{source}\n\n"
                "Respond with ONLY two lines:\n"
                "Time: <complexity>\n"
                "Space: <complexity>\n\n"
                "Use standard Big O notation. "
                "Space complexity = auxiliary space (exclude input)."
            ),
        }],
    )
    text = response.content[0].text.strip()  
    time_m = re.search(r'Time:\s*(O\([^)\n]+\))', text)
    space_m = re.search(r'Space:\s*(O\([^)\n]+\))', text)
    return {
        "time": time_m.group(1).strip() if time_m else "Unknown", # example: Time: O(n log n)
        "space": space_m.group(1).strip() if space_m else "Unknown",
    }

def boa(source, meta, testing_entry):
    if not testing_entry or not BIG_O_AVAILABLE:
        return None
    ns = {}
    exec(testing_entry["prompt"], ns) # stores in ns
    exec(source, ns) #read and store from ns

    solution =  ns['Solution']() # okay get class and initialize as a Solution class

    all_attributes = dir(solution) # returns a list of attributes and methods of the object
    public_methods = []
    for attribute in all_attributes:
        if not attribute.startswith('_'):
            public_methods.append(attribute)

    if not public_methods:
        return None

    method = getattr(solution, public_methods[0])


    response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=512,
            messages=[{
                "role": "user",
                "content": (
                    "Write a Python function `def gen(n):` returning a valid input tuple.\n\n"
                    f"Method signature:\n{meta['starter_code']}\n\n"
                    "Rules:\n"
                    "- n = input size (array length, node count, etc.)\n"
                    "- return a TUPLE of args matching method params (excluding self)\n"
                    "- tree_node(values) and list_node(values) helpers are available\n"
                    "- Return ONLY the function, no explanation, no markdown"
                ),
            }],
        )
    
    # extract gen_src
    gen_src = response.content[0].text # index into response, raw data
    if "```" in gen_src: # make sure it's not surrounded in ```
        gen_src = gen_src.split("```")[1]
        if gen_src.startswith("python"):
            gen_src = gen_src[len("python"):] # strip language tag
    gen_src = gen_src.strip() #strip whitespace
    exec(gen_src, ns) # append these parameters into ns


    def _timeout_handler(signum, frame): # LLM Gen
        raise TimeoutError("big_o timed out")
    signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(20)
    try:
        best, _ = big_o.big_o(lambda d: method(*d), ns['gen'], min_n=10, max_n=5000)
    finally:
        signal.alarm(0)
    
    time_complexity = {"time": EMPIRICAL_MAP.get(best.__class__.__name__, "Unknown")}
    return time_complexity