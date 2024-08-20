#!/usr/bin/python3

"""
Modules:
    - json: Provides functions to parse JSON strings and convert
    Python objects into JSON strings.
    - requests: Allows sending HTTP/1.1 requests with
    methods such as GET and POST.
    - sys: Provides access to some variables used or
    maintained by the Python interpreter, including `argv`.

Usage:
    The script can be run with command-line arguments passed via `sys.argv`.
    It typically makes HTTP requests and processes JSON responses.
"""

import json
import requests
import sys

response = requests.get('https://jsonplaceholder.typicode.com/todos')
response2 = requests.get('https://jsonplaceholder.typicode.com/users')

response_txt = json.loads(response.text)
response_txt2 = json.loads(response2.text)

user1 = []
tot_taks = []

if __name__ == "__main__":
    id = int(sys.argv[1])
    for usr in response_txt2:
        if usr['id'] == id:
            EMPLOYEE = usr['name']
    for todo in response_txt:
        
        if todo["userId"] == id:
            tasks = 0
            tot_taks.append(todo["title"])
            tasks = len(tot_taks)

        if todo["userId"] == id and todo["completed"] is True:
            user1.append(todo["title"])
            done = str(len(user1))

    user1 = " ".join(str(element) for element in user1)
    print(f'Employee {EMPLOYEE} is done with tasks({done}/{tasks}):\n{user1}')
