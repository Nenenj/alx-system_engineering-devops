#!/usr/bin/python3
"""
Retrieves employees' TODO list progress using a REST API.
"""

import requests
import sys


def fetch_employee_todo_progress(employee_id):
    # Base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Send a GET request to fetch user data
    user_response = requests.get(f"{base_url}users/{employee_id}")

    # Send a GET request to fetch TODO list data for the user
    todo_response = requests.get(f"{base_url}todos?userId={employee_id}")

    # Check if the requests were successful (status code 200)
    if (
        user_response.status_code != 200 or
        todo_response.status_code != 200
    ):
        print("Error fetching data.")
        return

    # Parse the JSON responses
    user_data = user_response.json()
    todo_data = todo_response.json()

    # Filter completed tasks
    completed_tasks = [task for task in todo_data if task["completed"]]
    num_completed_tasks = len(completed_tasks)
    total_num_tasks = len(todo_data)

    # Display employee progress
    print(
        "Employee {} is done with tasks ({}/{}):".format(
            user_data["name"],
            num_completed_tasks,
            total_num_tasks
        )
    )

    # Display completed tasks
    for task in completed_tasks:
        print("\t{}".format(task["title"]))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id)
