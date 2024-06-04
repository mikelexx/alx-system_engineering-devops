#!/usr/bin/python3
"""
queries the Reddit API and returns a list containing the titles of all
hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Args:
    subreddit: a group from which to get first 10 hot posts
    returns: titles of the all hot posts listed for a given subreddit.
    """
    payload = {'limit': 260}
    if str(after) == "None":
        return hot_list
    if len(after) > 0 and after != 'None':
        payload['after'] = after
    r = requests.get('https://www.reddit.com/r/{}/hot.json'.format(subreddit),
                     params=payload,
                     headers={'User-Agent': 'custom'})
    try:
        data = r.json()["data"]["children"]
        after = r.json()["data"]["after"]
        for post in data:
            hot_list.append(post["data"]["title"])
    except Exception:
        return None
    return recurse(subreddit, hot_list, after=after)
