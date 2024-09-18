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



tot_taks = []

if __name__ == "__main__":
    USER_ID = sys.argv[1]
    user = requests.get((response2 + f'/{USER_ID}')).json()
    username = user.get('username')
    todos = requests.get(response, params={"userId": USER_ID}).json()
    
    with open(f'{USER_ID}.csv', "w", newline="") as file :
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [USER_ID, username, t.get("completed"), t.get("title")]
         ) for t in todos]
    
            