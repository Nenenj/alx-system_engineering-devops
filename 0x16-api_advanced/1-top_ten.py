#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests
import sys


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    base_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(base_url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return

    data = response.json()
    posts = data.get("data", {}).get("children", [])
    for post in posts:
        title = post.get("data", {}).get("title")
        if title:
            print(title)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <subreddit>".format(sys.argv[0]))
        sys.exit(1)

    subreddit_name = sys.argv[1]
    top_ten(subreddit_name)
