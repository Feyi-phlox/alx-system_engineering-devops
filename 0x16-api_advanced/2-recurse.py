#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """recursive function that queries and returns titles of all hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                 after)
    headers = {"User-Agent": "linux:alx.api.project:v1.0.0 (by /u/feyi-phlox)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    result = response.json().get("data").get("children")
    for post in result:
        hot_list.append(post.get("data").get("title"))
    after = response.json().get("data").get("after")
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
