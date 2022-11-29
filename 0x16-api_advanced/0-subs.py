#!/usr/bin/python3
"""This python module contains a script that interacts with the Reddit API"""
from requests import get


def number_of_subscribers(subreddit):
    """Queries a reddit api and returns the number of subscribers for
    a given subredit"""
    header = {"User-Agent": "0x16.api.advanced.project:eleccrazy"}
    res = get("https://www.reddit.com/r/{}/about.json".format(subreddit),
              headers=header, allow_redirects=False)
    code = res.status_code
    return 0 if code == 404 else res.json().get("data").get("subscribers")
