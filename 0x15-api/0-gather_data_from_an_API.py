#!/usr/bin/python3

"""
Fetches and displays employee TODO list progress using the provided REST API.
"""

import requests
import sys


def fetch_employee_todo_list(employee_id):
    """
    Fetches and displays employee TODO list progress for a given employee ID.
    """
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = base_url + "users/{}".format(employee_id)
    todo_url = base_url + "todos"

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url, params={"userId": employee_id})

    print("User Response:", user_response.text)  # Print the user response
    print("Todo Response:", todo_response.text)  # Print the todo response

    if user_response.status_code == 200 and todo_response.status_code == 200:
        user_data = user_response.json()
        todo_data = todo_response.json()

        employee_name = user_data["name"]
        total_tasks = len(todo_data)
        completed_tasks = sum(1 for task in todo_data if task["completed"])

        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, completed_tasks, total_tasks))

        for task in todo_data:
            if task["completed"]:
                print("\t {}".format(task["title"]))
    else:
        print("Error fetching data.")
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_list(employee_id)
