#!/usr/bin/python3
"""This module containes a python script that interacts with the rest
api. For a given employee id, it returns information about his/her
TODO list progress."""
from requests import get
from sys import argv


if __name__ == "__main__":
    user_info = get('https://jsonplaceholder.typicode.com/users/{}'.
                    format(argv[1])).json()
    user_todos = get('https://jsonplaceholder.typicode.com/todos/',
                     params={"userId": argv[1]}).json()
    EMPLOYEE_NAME = user_info.get('name')
    NUMBER_OF_DONE_TASKS = len([task for task in user_todos
                               if task['completed']])
    TOTAL_NUMBER_OF_TASKS = len(user_todos)
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task in user_todos:
        if task['completed']:
            print('\t {}'.format(task['title']))
