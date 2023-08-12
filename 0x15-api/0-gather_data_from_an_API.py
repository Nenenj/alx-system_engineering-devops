#!/usr/bin/python3
"""
Retrieves information about an employee's TODO list progress using a REST API.
"""

import requests
import sys


def fetch_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(
        f"{base_url}users/{employee_id}"
    )
    todo_response = requests.get(
        f"{base_url}todos?userId={employee_id}"
    )

    if (
        user_response.status_code != 200 or
        todo_response.status_code != 200
    ):
        print("Error fetching data.")
        return

    user_data = user_response.json()
    todo_data = todo_response.json()

    completed_tasks = [task for task in todo_data if task["completed"]]
    num_completed_tasks = len(completed_tasks)
    total_num_tasks = len(todo_data)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            user_data["name"],
            num_completed_tasks,
            total_num_tasks
        )
    )

    for task in completed_tasks:
        print("\t{}".format(task["title"]))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id)
