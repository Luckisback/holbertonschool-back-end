#!/usr/bin/python3
"""using a rest API, for a given employee ID, returns
information about his/her TODO list progress
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":

    rows = []
    """ collects todos infos in a dict """
    r_todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    data_todos = r_todos.json()

    """ collect users infos in a dict """
    r_users = requests.get('https://jsonplaceholder.typicode.com/users/')
    data_users = r_users.json()

    """ gets the name of the employee """
    for i in data_users:
        if i.get("id") == int(argv[1]):
            employee = i.get("username")

    """ creates data in csv format """
    with open(argv[1] + '.csv', 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        # write results in rows
        for i in data_todos:
            rows = []
            if i.get("userId") == int(argv[1]):
                rows.append(i.get("userId"))
                rows.append(employee)
                rows.append(i.get("completed"))
                rows.append(i.get("title"))
                writer.writerow(rows)
