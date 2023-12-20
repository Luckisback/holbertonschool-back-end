#!/usr/bin/python3
"""using a rest API, for a given employee ID, returns
information about his/her TODO list progress
"""
import csv
import requests
from sys import argv

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

""" write results in rows """
for i in data_todos:
    row = []  # Create a new list for each TODO item
    if i.get("userId") == int(argv[1]):
        row.append(i.get("userId"))
        row.append(employee)
        row.append(i.get("completed"))
        row.append(i.get("title"))
        writer.writerow(row)
