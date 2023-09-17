#!/usr/bin/python3
"""Export API data to CSV"""

import requests
import csv
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

        # Create CSV file name
        csv_filename = f'{employee_id}.csv'

        # Write TODO list data to CSV file
        with open(csv_filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            
            # Write header row
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            
            # Write task data
            for task in todo_list:
                csv_writer.writerow([user_data['id'], user_data['username'], task['completed'], task['title']])

        print(f"Data exported to {csv_filename}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
