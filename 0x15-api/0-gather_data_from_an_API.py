#!/usr/bin/python3
"""Script using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import requests
import sys

def get_employee_todo_progress(employee_id):
    # Define the API URL
    base_url = 'https://jsonplaceholder.typicode.com/'
    todo_url = f'{base_url}todos'
    user_url = f'{base_url}users/{employee_id}'

    try:
        # Fetch user data
        user_response = requests.get(user_url)
        user_data = user_response.json()
        
        # Fetch user's TODO list
        todo_response = requests.get(todo_url, params={'userId': employee_id})
        todo_list = todo_response.json()

        # Count the number of completed tasks
        completed_tasks = [task for task in todo_list if task['completed']]
        num_completed_tasks = len(completed_tasks)
        total_tasks = len(todo_list)

        # Display employee TODO list progress
        print(f"Employee {user_data['name']} is done with tasks ({num_completed_tasks}/{total_tasks}):")
        
        # Display titles of completed tasks
        for task in completed_tasks:
            print(f"\t{task['title']}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

