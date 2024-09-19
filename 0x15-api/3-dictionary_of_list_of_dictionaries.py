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

response = 'https://jsonplaceholder.typicode.com/todos'
response2 = 'https://jsonplaceholder.typicode.com/users'

if __name__ == "__main__":
    all_data = {}
    url = requests.get(response2).json()
    USER_ID = [i.get('id') for i in url]
    for us in USER_ID:
        user = requests.get(response2 + f'/{us}').json()
        use = user.get('id')
        

        username = user.get('username')
        todos = requests.get(response, params={"userId": us}).json()
        
        all_data[us] = [{"task": t.get("title"),"completed": t.get("completed"), 
                         "username": username} for t in todos]
    
    with open('todo_all_employees.json', 'w', newline='') as jsonfile:
        json.dump(all_data, jsonfile)
