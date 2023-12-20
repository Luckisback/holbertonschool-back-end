#!/usr/bin/python3

""" The scrip that retrieves informations
    from an API link
"""

import json
import requests
import sys

user_id = int(sys.argv[1])

user_url = "https://jsonplaceholder.typicode.com/users"
user_info = requests.get(f"{user_url}/{user_id}").json()

EMPLOYEE_NAME = user_info.get("name")

if EMPLOYEE_NAME is None:
    print(f"Employee with ID {user_id} not found.")
    sys.exit(1)

todo_url = "https://jsonplaceholder.typicode.com/todos"
todo_info = requests.get(todo_url).json()

TASK_TITLE = []
TOTAL_NUMBER_OF_TASKS = 0
NUMBER_OF_DONE_TASKS = 0

for task in todo_info:
    if task.get("userId") == user_id:
        TOTAL_NUMBER_OF_TASKS += 1
        if task.get("completed"):
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(task.get("title"))

print("Employee {} is done with tasks ({}/{})".format(
    EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
