import json

# Load the two JSON files
with open('todo_all_employees.json', 'r') as f1, open('todo_all_employeesb.json', 'r') as f2:
    json_data1 = json.load(f1)
    json_data2 = json.load(f2)

# Compare the two JSON objects
if json_data1 == json_data2:
    print("The two JSON files are the same.")
else:
    print("The two JSON files are different.")

# Optional: If you want to print the differences
import difflib

with open('todo_all_employees.json', 'r') as f1, open('todo_all_employeesb.json', 'r') as f2:
    diff = difflib.unified_diff(
        f1.readlines(), f2.readlines(), fromfile='todo_all_employees.json', tofile='todo_all_employeesb.json'
    )
    for line in diff:
        print(line, end='')
