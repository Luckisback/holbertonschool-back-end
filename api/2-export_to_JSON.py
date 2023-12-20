#!/usr/bin/python3
"""export data in the JSON format using rest api
"""
import json
import requests
from sys import argv


if __name__ == "__main__":

    # collects todos infos in a dict
    r_todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    data_todos = r_todos.json()

    # collect users infos in a dict
    r_users = requests.get('https://jsonplaceholder.typicode.com/users/')
    data_users = r_users.json()

    rows = []
    for i in data_users:
        if i.get("id") == int(argv[1]):
            employee = i.get("username")
            id_number = i.get("id")

    for i in data_todos:
        new_dict = {}
        if i.get("userId") == int(argv[1]):
            new_dict["username"] = employee
            new_dict["task"] = i.get("title")
            new_dict["completed"] = i.get("completed")
            rows.append(new_dict)

    json_dict = {}
    json_dict[id_number] = rows
    json_obj = json.dumps(json_dict)
    with open(argv[1] + ".json", "w") as file:
        file.write(json_obj)
