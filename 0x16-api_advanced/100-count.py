#!/usr/bin/python3
"""recursive function that queries reddit API and
returns a list of all hot titles"""
import requests


def count_words(subreddit, word_list, count=None, after=None):
    """recursively queries the Reddit API and returns list of all hot titles"""
    if count is None:
        count = {}
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                 after)
    header = {"User-Agent": "linux:alx.api.project:v1.0.0 (by /u/feyi-phlox)"}
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json()
    posts = data['data']['children']

    if not posts:
        return count
    for post in posts:
        title = post['data']['title'].lower()
        for word in word_list:
            if word.lower() in title:
                if word in count:
                    count[word] += 1
                else:
                    count[word] = 1
    after = data['data']['after']
    if after:
        return count_words(subreddit, word_list, count, after)
    sort_count = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    for key, value in sort_count:
        print("{}: {}".format(key, value))
