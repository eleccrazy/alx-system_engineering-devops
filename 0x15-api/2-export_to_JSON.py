#!/usr/bin/python3
"""This module contains a python script that interacts with the REST api.
The script exports a given employee data into a json file format"""
from requests import get
from sys import argv
from json import dump


if __name__ == "__main__":
    user_info = get('https://jsonplaceholder.typicode.com/users/{}'.
                    format(argv[1])).json()
    user_todos = get('https://jsonplaceholder.typicode.com/todos/',
                     params={"userId": argv[1]}).json()

    USER_ID = str(user_info.get('id'))
    USERNAME = user_info.get('username')

    list_info = []

    for task in user_todos:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        task_info = {"task": TASK_TITLE, "completed": TASK_COMPLETED_STATUS,
                     "username": USERNAME}
        list_info.append(task_info)

    content = {USER_ID: list_info}

    file_name = USER_ID + ".json"

    with open(file_name, "w", encoding="utf8") as f:
        dump(content, f)
