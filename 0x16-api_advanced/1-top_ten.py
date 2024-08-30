#!/usr/bin/python3
""" function that queries and prints titles of first 10 hot posts
from reddit api listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """function that queries and prints titles of first 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "linux:alx.api.project:v1.0.0 (by /u/feyi-phlox)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print("None")
        return
    result = response.json().get("data").get("children")
    for post in result:
        print(post.get("data").get("title"))
