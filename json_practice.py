    
import json

json_data ='''[
    {
        "number": 1,
        "task": "pray"
    }
    {
        "number": 2,
        "task": "code the project"
    },
    {
        "number": 3,
        "task": "make coffee"
    }
]'''

try:
    python_data = json.loads(json_data)
except json.JSONDecodeError as error:
    print(f"Invalid JSON from model: {error}")   
else:    
    for task in python_data:
        print(f"{task['number']}. {task['task']}")


    