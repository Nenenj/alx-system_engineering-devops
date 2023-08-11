#!/usr/bin/python3
"""Export API data to CSV"""

import csv
import requests as r
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'

    user_data = r.get(url + "users/{}".format(user_id)).json()
    username = user_data.get("username")
    todo_data = r.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow([user_id, username, elm.get("completed"),
                          elm.get("title")]) for elm in to_do]
