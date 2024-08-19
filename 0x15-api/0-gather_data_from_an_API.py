#!/usr/bin/python3

import json
import requests
from sys import argv

response = requests.get('https://jsonplaceholder.typicode.com/todos')
response2 = requests.get('https://jsonplaceholder.typicode.com/users')

response_txt = json.loads(response.text)
response_txt2 = json.loads(response2.text)

user1 = []
tot_taks = []

if __name__ == "__main__":
    id = argv[1]
    for todo in response_txt:
        tasks = 0
        if todo["userId"] == int(id):
            tot_taks.append(todo["title"])
            tasks = len(tot_taks)

        if todo["userId"] == int(id) and todo["completed"] is True:
            user1.append(todo["title"])
            done = str(len(user1))

    print(f'Employee {EMPLOYEE} is done with tasks({done}/{tasks}):\n{user1}')
