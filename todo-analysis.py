# iterate through every difficulty dir, every problem dir

# generate a {question_id}_report.md in the filepath

### import current human_gen code for analysis
### import current claude_gen code for analysis

# Then, analyze time and space complexity of human and claude

### Part 1 - AST - Abstract Tree Syntax
# Use AST library to statically analyze code. Store result in a NESTED DICT

### Part 2 - Claude
# Ping claude API to analyze time and space complexity, seeing if it agrees with AST


### Part 3 - Merge
# If they agree... good
# If they disagree... favor claude, and FLAG the discrepency in the .md


# place the verdict of analysis in the report.md that lives in each question dir