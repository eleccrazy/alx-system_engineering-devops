#!/usr/bin/python3
"""This module contains a python script that interacts with the REST api.
The script exports a given employee data into a json file format"""
from requests import get
from json import dump


if __name__ == "__main__":
    users = get('https://jsonplaceholder.typicode.com/users')

    content = {}
    for user in users.json():
        USER_ID = str(user.get('id'))
        user_info = get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(USER_ID)).json()
        user_todos = get('https://jsonplaceholder.typicode.com/todos/',
                         params={"userId": USER_ID}).json()
        USERNAME = user_info.get('username')

        list_info = []

        for task in user_todos:
            TASK_COMPLETED_STATUS = task.get('completed')
            TASK_TITLE = task.get('title')
            task_info = {"task": TASK_TITLE,
                         "completed": TASK_COMPLETED_STATUS,
                         "username": USERNAME}
            list_info.append(task_info)

        content[USER_ID] = list_info

    with open("todo_all_employees.json", "w", encoding="utf8") as f:
        dump(content, f)
