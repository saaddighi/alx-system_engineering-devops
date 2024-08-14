#!/usr/bin/python3

import requests 
import json

response = requests.get('https://jsonplaceholder.typicode.com/todos')
response2 = requests.get('https://jsonplaceholder.typicode.com/users')

response_txt = json.loads(response.text)
response_txt2 = json.loads(response2.text)

user1 = []
tot_taks = []

for users in response_txt2:
    EMPLOYEE_NAME = users['name']
    id = users['id']
    for todo in response_txt:
        tasks = 0
        if todo["userId"] == int(id):
            tot_taks.append(todo["title"])
            tasks = len(tot_taks)

        if todo["userId"] == int(id) and todo["completed"] == True:
            user1.append(todo["title"])
            done_tasks = str(len(user1))
        
    print(f'Employee {EMPLOYEE_NAME} is done with tasks({done_tasks}/{tasks}):\n{user1}')
    
