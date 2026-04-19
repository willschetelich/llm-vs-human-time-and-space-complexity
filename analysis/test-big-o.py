import json
import big_o
import anthropic

# 1. Load problem from testing.json (has 'prompt' field)
with open("testing.json") as f:
    testing_data = json.load(f)

problem = next(p for p in testing_data if p['question_id'] == 100)

with open("easy/100/easy_100_qiyuangong.py") as f:
    solution_source = f.read()

# 2. Link in prompt (namespace with all dependencies)
namespace = {}
exec(problem['prompt'], namespace)
exec(solution_source, namespace)
method = namespace['Solution']().isSameTree

print("Solution loaded successfully")

# 3. Claude generates gen(n)
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=512,
    messages=[{
        "role": "user",
        "content": f"""Write a Python function `def gen(n):` that returns a valid input tuple for this LeetCode method.

Method signature:
{problem['starter_code']}

Rules:
- n is the size of the input (number of nodes, array length, etc.)
- return a TUPLE of args matching the method parameters (excluding self)
- tree_node(values: list) builds a whole tree from a list e.g. tree_node([1,2,3])
- list_node(values: list) builds a linked list from a list e.g. list_node([1,2,3])
- TreeNode(val) creates a single node
- return ONLY the function definition, no explanation, no markdown
"""
    }]
)

gen_source = response.content[0].text
# strip markdown code fences if present
if "```" in gen_source:
    gen_source = gen_source.split("```")[1]
    if gen_source.startswith("python"):
        gen_source = gen_source[len("python"):]
gen_source = gen_source.strip()
print("gen(n) source:\n", gen_source)

exec(gen_source, namespace)
gen = namespace['gen']

# 4. Feed to big_o
def wrapped(data):
    return method(*data)

best, _ = big_o.big_o(wrapped, gen, min_n=10, max_n=10000)

COMPLEXITY_MAP = {
    'Constant': 'O(1)',
    'Logarithmic': 'O(log n)',
    'Linear': 'O(n)',
    'Linearithmic': 'O(n log n)',
    'Quadratic': 'O(n²)',
    'Cubic': 'O(n³)',
    'Polynomial': 'O(n^k)',
    'Exponential': 'O(2^n)',
}

complexity = COMPLEXITY_MAP.get(best.__class__.__name__, 'Unknown')
print("Time complexity:", complexity)
