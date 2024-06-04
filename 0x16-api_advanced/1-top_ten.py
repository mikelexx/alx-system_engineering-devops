#!/usr/bin/python3
"""
contains function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Args:
    subreddit: a group from which to get first 10 hot posts
    returns: titles of the first 10 hot posts listed for a given subreddit.
    """
    payload = {'limit': 9}
    r = requests.get('https://www.reddit.com/r/{}/hot.json'.format(subreddit),
                     params=payload,
                     headers={'User-Agent': 'custom'})
    try:
        data = r.json()["data"]["children"]
        for post in data:
            print(post["data"]["title"])
    except Exception:
        print("None")
