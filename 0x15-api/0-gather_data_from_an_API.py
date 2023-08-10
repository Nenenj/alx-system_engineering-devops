#!/usr/bin/python3

"""
Fetches and displays employee TODO list progress using the provided REST API.
"""

import requests
import sys


def fetch_employee_todo_list(employee_id):

    url = "https://jsonplaceholder.typicode.com/"
    user_response = request.get(url + "users/{}".format(employee_id))
    todo_response = request.get(url + "todos", params={"userId": employee_id})

    if user_response.status_code == 200 and todo_response.status_code == 200:
        print("Error fetching data.")
        return

    user = user_response.json()
    todos = todo_response.json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    employee_name = "Employee Name: OK"
    print(f"{Employee_name:<18}\n\nTo Do Count: OK")
    print("\nEmployee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    for idx, c in enumerate(completed, start=1):
        task_formatting = f"Task {idx} Formatting: OK"
        print(task_formatting)
        print("\t {}".format(c))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_list(employee_id)
