#!/usr/bin/python3
"""This python module contains a script that interacts with the Reddit API"""
from requests import get


def top_ten(subreddit):
    """Queries the reddit api and prints the titles of the first 10
    hot posts."""
    param = {"limit": 10}
    header = {"User-Agent": "0x16.api.advanced.project:eleccrazy"}
    res = get("https://www.reddit.com/r/{}/hot/.json".format(subreddit),
              headers=header, allow_redirects=False, params=param)
    if res.status_code == 404:
        print("None")
    else:
        for r in res.json().get("data").get("children"):
            print(r.get("data").get("title"))
