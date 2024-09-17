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

import csv
import json
import requests
import sys

response = requests.get('https://jsonplaceholder.typicode.com/todos')
response2 = requests.get('https://jsonplaceholder.typicode.com/users')

response_txt = json.loads(response.text)
response_txt2 = json.loads(response2.text)

tot_taks = []

if __name__ == "__main__":
    USER_ID = int(sys.argv[1])
    for usr in response_txt2:
        if usr['id'] == USER_ID:
            USERNAME = usr['username']
    for todo in response_txt:
        if todo["userId"] == USER_ID:
            TASK_TITLE = todo["title"]
            TASK_COMPLETED_STATUS = todo["completed"]
            row = USER_ID,USERNAME,TASK_COMPLETED_STATUS,TASK_TITLE
            tot_taks.append(row)

        with open('USER_ID.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            for row in tot_taks:
                writer.writerows(tot_taks)
