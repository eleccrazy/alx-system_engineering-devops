#!/usr/bin/python3
"""This module contains a python script that interacts with the REST api.
The script exports a given employee data into a CSV file format"""
from requests import get
from sys import argv
from csv import writer, QUOTE_ALL


if __name__ == "__main__":
    user_info = get('https://jsonplaceholder.typicode.com/users/{}'.
                    format(argv[1])).json()
    user_todos = get('https://jsonplaceholder.typicode.com/todos/',
                     params={"userId": argv[1]}).json()

    USER_ID = str(user_info.get('id'))
    USERNAME = user_info.get('username')

    for task in user_todos:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')

        info_list = [USER_ID, USERNAME, TASK_COMPLETED_STATUS,
                     TASK_TITLE]
        file_name = USER_ID + '.csv'

        with open(file_name, "a") as f:
            w = writer(f, quoting=QUOTE_ALL)
            w.writerow(info_list)
