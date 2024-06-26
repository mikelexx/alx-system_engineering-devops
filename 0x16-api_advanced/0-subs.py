#!/usr/bin/python3
"""
Contains function for retrieving subscribers from subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Args:
    subreddit: subreddit from which to get number of subscribers.
    return: returns the number of subscribers (not active users,
    total subscribers) for a given subreddit
    """
    r = requests.get(
        'https://www.reddit.com/r/{}/about.json'.format(subreddit),
        headers={'User-Agent': 'mike'})
    if r.status_code == 200:
        data = r.json().get("data").get("subscribers")
        return data
    else:
        return (0)
