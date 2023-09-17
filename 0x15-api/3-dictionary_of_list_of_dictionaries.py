#!/usr/bin/python3
"""python script to fetch Rest API for todo lists of employees"""

import requests
import json

def export_todo_data_to_json():
    # Define the API URL
    base_url = 'https://jsonplaceholder.typicode.com/'
    users_url = f'{base_url}users'
    todos_url = f'{base_url}todos'

    try:
        # Fetch user data
        users_response = requests.get(users_url)
        users_data = users_response.json()

        # Fetch TODO list data
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Create a dictionary to store data for all employees
        all_employees_data = {}

        # Populate the dictionary with employee data
        for user in users_data:
            user_id = user['id']
            username = user['username']
            user_tasks = []

            # Find tasks for the current user
            for task in todos_data:
                if task['userId'] == user_id:
                    user_task = {
                        'username': username,
                        'task': task['title'],
                        'completed': task['completed']
                    }
                    user_tasks.append(user_task)

            all_employees_data[user_id] = user_tasks

        # Create JSON file
        json_filename = 'todo_all_employees.json'
        with open(json_filename, 'w') as json_file:
            json.dump(all_employees_data, json_file, indent=4)

        print(f"Data exported to {json_filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    export_todo_data_to_json()
