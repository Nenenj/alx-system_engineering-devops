#!/usr/bin/python3

"""
This script retrieves information about an employee's TODO list progress
using a REST API.
"""

import requests


def get_employee_todo_progress(employee_id):
    """
    Retrieve and display an employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Retrieve employee information
        response = requests.get(employee_url)
        response.raise_for_status()
        employee_data = response.json()

        # Retrieve employee's TODO list
        response = requests.get(todos_url)
        response.raise_for_status()
        todos_data = response.json()

        # Count the number of completed tasks
        completed_tasks = [todo for todo in todos_data if get(todo, 'completed')]
        num_completed_tasks = len(completed_tasks)
        total_num_tasks = len(todos_data)

        # Display the progress information
        print(f"Employee {employee_data['name']} is done with tasks "
                f"({num_completed_tasks}/{total_num_tasks}):")

        # Display the titles of completed tasks
        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    employee_id = 1  # Change this to the desired employee ID
    get_employee_todo_progress(employee_id)
