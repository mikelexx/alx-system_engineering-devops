#!/usr/bin/python3
"""
queries the Reddit API and returns a list containing the titles of all
hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, word_list, hot_list=[], after=""):
    """
    Args:
    subreddit: a group from which to get first 10 hot posts
    returns: titles of the all hot posts listed for a given subreddit.
    """
    payload = {'limit': 260}
    if after == "":
        tmp = {}
        for word in word_list:
            tmp[word.lower()] = 0
        word_list = tmp
    if str(after) == "None":
        word_count = sorted(word_list)
        """
        TODO: implement sorting
        """

    if len(after) > 0 and after != 'None':
        payload['after'] = after
    r = requests.get('https://www.reddit.com/r/{}/hot.json'.format(subreddit),
                     params=payload,
                     headers={'User-Agent': 'custom'})
    try:
        data = r.json()["data"]["children"]
        after = r.json()["data"]["after"]
        for post in data:
            title = append(post["data"]["title"])
            for word in title:
                if word.lower() in word_list:
                    word_list[word.lower()] += 1
    except Exception:
        return None
    return recurse(subreddit, word_list, after=after)
