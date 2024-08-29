#!/usr/bin/python3
""" Module that that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0 """
import requests


def number_of_subscribers(subreddit):
    """this queries the Reddit API and returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {"User-agent": "feyi-phlox"}
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code != 200:
        return 0
    result = response.json()
    return result["data"]["subscribers"]
