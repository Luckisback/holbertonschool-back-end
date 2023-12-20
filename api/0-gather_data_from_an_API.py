#!/usr/bin/python3
"""using a rest API, for a given employee ID, returns
information about his/her TODO list progress
"""
import requests
from sys import argv


if __name__ == "__main__":

    TOTAL_NUMBER_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    # collects todos infos in a dict
    r_todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    data_todos = r_todos.json()

    # collect users infos in a dict
    r_users = requests.get('https://jsonplaceholder.typicode.com/users/')
    data_users = r_users.json()

    for i in data_todos:
        # check how many total tasks there are for the given user id
        if i.get("userId") == int(argv[1]):
            TOTAL_NUMBER_OF_TASKS += 1
            # check how many tasks he has done
            if i.get("completed") is True:
                NUMBER_OF_DONE_TASKS += 1
                # appends the title of the completed task to a list
                TASK_TITLE.append(i.get("title"))

    # collect the name of the employee
    for i in data_users:
        if i.get("id") == int(argv[1]):
            employee = i.get("name")

    # print result to the correct format
    print("Employee {} is done with tasks({}/{}):".format(
        employee, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for titles in TASK_TITLE:
        print("\t {}".format(titles))
